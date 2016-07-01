# -*- coding:utf-8 -*-

def make_code_table(input_file_name, output_file_name):
    try:
        # input raw data
        fin = open(input_file_name, "r")
        raw = fin.readlines()
        fin.close()
        # sort by frequency
        list_by_freqency = list()
        for line in raw:
            list_by_freqency.append([float(line[2:]), [[line[0],""],]])
        list_by_freqency.sort(reverse=True)
        # check, not necessary
        cnt = 0.0
        for line in list_by_freqency:
            print line
            cnt += line[0]
        print "Total frequency:", cnt, "%"
        # encode
        while len(list_by_freqency) > 1:
            char1 = list_by_freqency.pop()
            for char in char1[1]:
                char[1] = "1" + char[1]

            char2 = list_by_freqency.pop()
            for char in char2[1]:
                char[1] = "0" + char[1]

            new_char = [char1[0]+char2[0], char1[1]+char2[1]]
            list_by_freqency.append(new_char)
            list_by_freqency.sort(reverse=True)

        encode_char = list_by_freqency[0][1]
        encode_char.sort()
        # check, not necessary
        for line in encode_char:
            print line
        # write output-file
        fout = open(output_file_name, "w+")
        for line in encode_char:
            fout.write("%s %s\n"%(line[0], line[1]))
        fout.close()

    except Exception, e:
        raise e


# this function only support to encode characters who exist in code table
def encode(code_table, input_file_name, output_file_name, mod_x):
    try:
        # input code table and file which needs to be encoded
        fcode = open(code_table,'r')
        raw_table = fcode.readlines()
        fcode.close()

        fin = open(input_file_name, "r")
        raw_file = fin.read()
        fin.close()
        # encode
        code_table = dict()
        for line in raw_table:
            code_table[line[0]] = line[2:-1]

        encoded_file = str()
        for i in raw_file:
            encoded_file = encoded_file + code_table[i]
        num = len(encoded_file) % mod_x
        for i in range(num):
            encoded_file = encoded_file + "0"
        # check, not necessary
        print code_table
        print encoded_file
        print "length after encode:", len(encoded_file)
        print "mod %d:"%mod_x, num
        # write output-file
        f = open(output_file_name, "w+")
        f.write(encoded_file)
        f.close()

    except Exception, e:
        raise e


def efficiency(code_table, input_file_name):
    from math import log, e
    try:
        # input code table and file which needs to be encoded
        fcode = open(code_table,'r')
        raw_table = fcode.readlines()
        fcode.close()

        fin = open(input_file_name, "r")
        raw_file = fin.readlines()
        fin.close()
        
        code_length = dict()
        for line in raw_table:
            code_length[line[0]] = len(line[2:-1])

        code_frequency = dict()
        for line in raw_file:
            code_frequency[line[0]] = float(line[2:])/100
        # average code length
        average_code_length = float()
        for i in code_length.keys():
            average_code_length += code_length[i] * code_frequency[i]
        # source entropy
        source_entropy = float()
        for i in code_frequency.keys():
            source_entropy += -(code_frequency[i] * log(code_frequency[i]) / log(e))
        # encode efficiency
        encode_efficiency = source_entropy / average_code_length * 100
        # check, not necessary
        print "source entropy:", source_entropy
        print "average code length:", average_code_length
        print "encode efficiency:", encode_efficiency, "%"

    except Exception, e:
        raise e


def decode(code_table, input_file_name, output_file_name):
    try:
        # input code table and file which needs to be decoded
        fcode = open(code_table,'r')
        raw_table = fcode.readlines()
        fcode.close()
        fin = open(input_file_name, "r")
        raw_file = fin.read()
        fin.close()
        # decode
        code_table = dict()
        for line in raw_table:
            code_table[line[2:-1]] = line[0]

        decoded_file = str()
        tmp = str()
        for char in raw_file:
            tmp = tmp + char
            if tmp in code_table:
                decoded_file = decoded_file + code_table[tmp]
                tmp = str()
        # check, not necessary
        print decoded_file
        # write output-file
        f = open(output_file_name, "w+")
        f.write(decoded_file)
        f.close()

    except Exception, e:
        raise e


#test if function is correct
if __name__ == "__main__":
    make_code_table("frequency.txt", "huffman_table_out.txt")
    encode("huffman_table_out.txt", "raw_file.txt", "huffman_out.txt", 4)
    decode("huffman_table_out.txt", "huffman_out.txt", "huffman_decode_out.txt")
    print "================="
    efficiency("huffman_table_out.txt", "frequency.txt")