# -*- coding:utf-8 -*-
X = [[0,0,0,0],
     [0,0,0,1],
     [0,0,1,0],
     [0,0,1,1],
     [0,1,0,0],
     [0,1,0,1],
     [0,1,1,0],
     [0,1,1,1],
     [1,0,0,0],
     [1,0,0,1],
     [1,0,1,0],
     [1,0,1,1],
     [1,1,0,0],
     [1,1,0,1],
     [1,1,1,0],
     [1,1,1,1]]

G = [[1, 0, 0, 0, 0, 1, 1],
     [0, 1, 0, 0, 1, 0, 1],
     [0, 0, 1, 0, 1, 1, 0],
     [0, 0, 0, 1, 1, 1, 1]]

H = [[0, 0, 0, 1, 1, 1, 1],
     [0, 1, 1, 0, 0, 1, 1],
     [1, 0, 1, 0, 1, 0, 1]]

E = [[1, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 1]]


def make_code_table(output_file_name):
    try:
        # initiate 
        C = list()
        for i in range(len(X)):
            ci = str()
            for j in range(len(E)):
                num = 0
                for k in range(len(G)):
                    if(X[i][k]==G[k][j])and(X[i][k]!=0) : 
                        num += 1
                ci = ci + str(num % 2)
            C.append(ci)
        # check, not necessary
        # for line in C: print line
        # write output-file
        fout = open(output_file_name, "w+")
        for i in range(len(C)):
            s2 = str()
            for j in range(len(G)):
                s2 = s2 + str(X[i][j])
            fout.write("%s %s\n"%(s2, C[i]))
        fout.close()

    except Exception, e:
        raise e


def error_flag(output_file_name):
    # initiate error flag
    S = list()
    for i in range(len(E)):
        si = str()
        for j in range(len(H)):
            num = 0
            for k in range(len(E)):
                if(E[i][k]==H[j][k])and(E[i][k]!=0) : 
                    num += 1
            si = si + str(num % 2)
        S.append(si)
    # check, not necessary
    # for line in S: print line
    # write output-file
    f = open(output_file_name, "w+")
    f.write("000 0000000\n")
    for i in range(len(E)):
        s2 = str()
        for j in range(len(E)):
            s2 = s2 + str(E[i][j])
        f.write("%s %s\n"%(S[i], s2))
    f.close()


def encode(code_table, input_file_name, output_file_name):
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
            code_table[line[0:4]] = line[5:-1]

        encoded_file = str()
        for i in range(len(raw_file)/4):
            encoded_file = encoded_file + code_table["".join(raw_file[4*i:4*i+4])]
        # check, not necessary
        # print code_table
        # print encoded_file
        # write output-file
        f = open(output_file_name, "w+")
        f.write(encoded_file)
        f.close()

    except Exception, e:
        raise e


def check(character, code_table):
    try:
        # input code table and character which needs to be checked
        fcode = open(code_table,'r')
        raw_table = fcode.readlines()
        fcode.close()

        ri = list(character)

        si = str()
        for i in range(len(H)):
            tmp = 0
            for j in range(len(ri)):
                if (ri[j]==str(H[i][j]))and(ri[j]=="1"):
                    tmp += 1
            si = si + str(tmp % 2)

        # check
        code_table = dict()
        for line in raw_table:
            code_table[line[0:3]] = line[4:-1]

        ei = code_table[si]
        # print "A", si, ei, "".join(ri)
        for i in range(len(ei)):
            ri[i] = str(int(ei[i]) ^ int(ri[i]))
        # print "B", si, ei, "".join(ri)
        return "".join(ri)

    except Exception, e:
        raise e


def decode(code_table, input_file_name, output_file_name, error_flag):
    mark = str()
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
            code_table[line[5:-1]] = line[0:4]

        decoded_file = str()
        for i in range(len(raw_file)/7):
            mark = "".join(raw_file[7*i:7*i+7]) + "\n" + check("".join(raw_file[7*i:7*i+7]), error_flag)
            decoded_file = decoded_file + code_table[check("".join(raw_file[7*i:7*i+7]), error_flag)]
        # check, not necessary
        # print code_table
        # print decoded_file
        print "[*]Length after Hanmming decode:", len(decoded_file)
        # write output-file
        f = open(output_file_name, "w+")
        f.write(decoded_file)
        f.close()

    except Exception, e:
        print "==========================="
        print mark
        print "+++++++++++++++++++++++++++"
        raise e


#test if function is correct
if __name__ == "__main__":
    error_flag("error_flag.txt")
    make_code_table("hamming_table_out.txt")
    encode("hamming_table_out.txt", "huffman_out.txt", "hamming_out.txt")
    decode("hamming_table_out.txt", "hamming_out.txt", "hamming_decode_out.txt")
    import Huffman
    Huffman.decode("huffman_table_out.txt", "hamming_decode_out.txt", "huffman_decode_out.txt")