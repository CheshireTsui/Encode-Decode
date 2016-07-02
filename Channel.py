# -*- coding:utf-8 -*-
Z = [[1.0, 0.0],
     [0.1, 0.9]]

def transmission(input_file_name, output_file_name):
    from random import random
    try:
        # input file which needs transmission
        fin = open(input_file_name, "r")
        raw_file = fin.read()
        fin.close()
        # fake transmission
        message_out = str()
        for i in raw_file:
            if random() > Z[int(i)][0]:
                message_out = message_out + "1"
            else:
                message_out = message_out + "0"
        # check, not necessary
        # print message_out
        print "[*]Length after transport:", len(message_out)
        # write output-file
        f = open(output_file_name, "w+")
        f.write(message_out)
        f.close()

    except Exception, e:
        raise e


#test if function is correct
if __name__ == "__main__":
    transmission("hamming_out.txt", "channel_out.txt")
    import Hamming, Huffman
    # Hamming is decoding ;D
    Hamming.decode("hamming_table_out.txt", "channel_out.txt", "hamming_decode_out_from_channel.txt")
    # Huffman is decoding XD
    Huffman.decode("huffman_table_out.txt", "hamming_decode_out_from_channel.txt", "huffman_decode_out_from_channel.txt")