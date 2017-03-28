import numpy as np;
from householder import *

def bidiagonal(A):
    n = A.shape[0]
    m = A.shape[1]
    
    Qleft = np.eye(n,n)
    Qright = np.eye(n,n)
    BD = A
    print "BD\n", BD

    for i in range(n-1):
        X = BD[i:n, i]
        print "i =", i
        # Y vector with a single non-zero element
        Y = np.matrix(np.zeros([n-i,1]))
        Y[0,0] = np.linalg.norm(X)
        
        U = np.zeros([n, 1])
        U[i:n] = calculate_householder_vector(X, Y)
        BD = 

        if i != m-2:
            X = BD[i, (i+1):m]
           
