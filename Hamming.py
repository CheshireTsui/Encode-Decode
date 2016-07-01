# -*- coding:utf-8 -*-
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

def error_flag(file_name):
    #initiate error flag
    S = list()
    for i in range(len(E)):
        si = list()
        for j in range(len(H)):
            num = 0
            for k in range(len(E)):
                if(E[i][k]==H[j][k])and(E[i][k]!=0) : 
                    num = 1
                    break
            si.append(num)
        S.append(si)
    # check, not necessary
    for line in S: print line
    # write output-file
    f = open(file_name, "w+")
    for i in range(len(E)):
    	s1 = str()
    	s2 = str()
        for j in range(len(H)):
            s1 = s1 + str(S[i][j])
        for j in range(len(E)):
            s2 = s2 + str(E[i][j])
        f.write("%s %s\n"%(s1, s2))
    f.close()




#test if function is correct
if __name__ == "__main__":
    error_flag("error_flag.txt")