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
                        num = 1
                        break
                ci = ci + str(num)
            C.append(ci)
        # check, not necessary
        for line in C: print line
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
                    num = 1
                    break
            si = si + str(num)
        S.append(si)
    # check, not necessary
    for line in S: print line
    # write output-file
    f = open(output_file_name, "w+")
    for i in range(len(E)):
        s2 = str()
        for j in range(len(E)):
            s2 = s2 + str(E[i][j])
        f.write("%s %s\n"%(S[i], s2))
    f.close()




#test if function is correct
if __name__ == "__main__":
    error_flag("error_flag.txt")
    make_code_table("hamming_table_ouy.txt")