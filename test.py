# -*- coding:utf-8 -*-

import Huffman, Hamming, Channel

#test if function is correct
if __name__ == "__main__":
    # Huffman is encoding XD
    Huffman.make_code_table("frequency.txt", "huffman_table.out")
    Huffman.encode("huffman_table.out", "raw_file.txt", "huffman.out", 4)
    # Hamming is encoding ;D
    print "=====message with Hamming-coding====="
    Hamming.error_flag("error_flag.out")
    Hamming.make_code_table("hamming_table.out")
    Hamming.encode("hamming_table.out", "huffman.out", "hamming.out")
    # message is in the channel
    Channel.transmission("hamming.out", "channel.out")
    # Hamming is decoding ;D
    Hamming.decode("hamming_table.out", "channel.out", "hamming_decode_out_from_channel.out", "error_flag.out")
    # Huffman is decoding XD
    Huffman.decode("huffman_table.out", "hamming_decode_out_from_channel.out", "huffman_decode_out_from_channel.out")
    print "=====message *without* Hamming-coding====="
    # message is in the channel
    Channel.transmission("hamming.out", "channel.out")
    # Huffman is decoding XD
    Huffman.decode("huffman_table.out", "channel.out", "huffman_decode_out_from_channel2.out")
    print "=====Huffman====="
    Huffman.efficiency("huffman_table.out", "frequency.txt")