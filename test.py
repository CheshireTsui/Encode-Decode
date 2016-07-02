# -*- coding:utf-8 -*-

import Huffman, Hamming, Channel

#test if function is correct
if __name__ == "__main__":
	# Huffman is encoding XD
    Huffman.make_code_table("frequency.txt", "huffman_table_out.txt")
    Huffman.encode("huffman_table_out.txt", "raw_file.txt", "huffman_out.txt", 4)
    # Hamming is encoding ;D
    print "=====message with Hamming-coding====="
    Hamming.error_flag("error_flag.txt")
    Hamming.make_code_table("hamming_table_out.txt")
    Hamming.encode("hamming_table_out.txt", "huffman_out.txt", "hamming_out.txt")
    # message is in the channel
    Channel.transmission("hamming_out.txt", "channel_out.txt")
    # Hamming is decoding ;D
    Hamming.decode("hamming_table_out.txt", "channel_out.txt", "hamming_decode_out_from_channel.txt")
    # Huffman is decoding XD
    Huffman.decode("huffman_table_out.txt", "hamming_decode_out_from_channel.txt", "huffman_decode_out_from_channel.txt")
    print "=====message *without* Hamming-coding====="
    # message is in the channel
    Channel.transmission("hamming_out.txt", "channel_out.txt")
    # Huffman is decoding XD
    Huffman.decode("huffman_table_out.txt", "channel_out.txt", "huffman_decode_out_from_channel2.txt")
    print "=====Huffman====="
    Huffman.efficiency("huffman_table_out.txt", "frequency.txt")