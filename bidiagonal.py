import numpy as np;
from householder import *

def bidiagonal(A):
    n = A.shape[0]
    Qleft = np.eye(n,n)
    Qright = np.eye(n,n)
    BD = A
    print "BD\n", BD

    for i in range(n):
        X = BD[i:n,i]
        print "i =", i
        # Y vector with a single non-zero element
        Y = np.matrix(np.zeros([n-i,1]))
        Y[0,0] = 1
        # Q1 maps X on Y
        Q1 = householder(X, Y)
        print "Q1\n", Q1

####################################################
# Tests

A = np.matrix( [[1, 5, 3, 2],
                [3, 6, 4, 1],
                [2, 1, 0, 7]] )
bidiagonal(A)
