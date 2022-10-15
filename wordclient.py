from struct import pack
import sys
import socket

# How many bytes is the word length?
WORD_LEN_SIZE = 2

def usage():
    print("usage: wordclient.py server port", file=sys.stderr)

packet_buffer = b''

def get_next_word_packet(s):
    """
    Return the next word packet from the stream.

    The word packet consists of the encoded word length followed by the
    UTF-8-encoded word.

    Returns None if there are no more words, i.e. the server has hung
    up.

        while True:
        if buffer starts with a complete packet
            extract the packet data
            strip the packet data off the front of the buffer
            return the packet data

        receive more data

        if amount of data received is zero bytes
            return connection closed indicator

        append received data onto the buffer
    """

    global packet_buffer
    next_word = b''

    # TODO -- Write me!

    while True:
        # if i have complete packet then slice
        if len(packet_buffer) >= 2:
            word_length = int.from_bytes(packet_buffer[:2], "big")
            packet_size = word_length + 2
            if packet_size <= len(packet_buffer):
                packet = packet_buffer[:packet_size]
                packet_buffer = packet_buffer[packet_size:]
                return packet 
        chunk = s.recv(5)
        if len(chunk) == 0:
            return None
        packet_buffer += chunk
        
        


def extract_word(word_packet):
    """
    Extract a word from a word packet.

    word_packet: a word packet consisting of the encoded word length
    followed by the UTF-8 word.

    Returns the word decoded as a string.
    """

    # TODO -- Write me!

    return word_packet[2:].decode()

# Do not modify:

def main(argv):
    try:
        host = argv[1]
        port = int(argv[2])
    except:
        usage()
        return 1

    s = socket.socket()
    s.connect((host, port))

    print("Getting words:")

    while True:
        word_packet = get_next_word_packet(s)

        if word_packet is None:
            break

        word = extract_word(word_packet)

        print(f"    {word}")

    s.close()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
