import numpy as np;
from householder import *

# Mise sous forme bidiagonale
def bidiagonal(A):
    n = A.shape[0]
    m = A.shape[1]
    
    Qleft = np.matrix(np.eye(n,n))
    Qright = np.matrix(np.eye(m,m))
    BD = A

    for i in range(n):

        if i < m:
            X = BD[i:n, i]
            # Y vector with a single non-zero element
            Y = np.matrix(np.zeros([n-i,1]))
            Y[0,0] = np.linalg.norm(X)
            
            U1 = np.zeros([n, 1])
            U1[i:n] = calculate_householder_vector(X, Y)
            Qleft = optimized_matrix_product_AxH(Qleft, U1)
            BD = optimized_matrix_product_HxA(U1, BD)

        if i < m-2:
            X = BD[i, (i+1):m]
            X = np.transpose(X)
            Y = np.matrix(np.zeros([m-i-1,1]))
            Y[0,0] = np.linalg.norm(X)

            U2 = np.zeros([m, 1])
            U2[(i+1):m] = calculate_householder_vector(X, Y)
            Qright = optimized_matrix_product_HxA(U2, Qright)
            BD = optimized_matrix_product_AxH(BD, U2)

    return Qleft, BD, Qright

# tests to remove
A = np.matrix( [[1, 5],
                [3, 6],
                [2, 1]] )


def print_m(A):

    (n,m) = A.shape
    print "\n"
    for i in range(n):

        for j in range(m):

            if (abs(A[i,j]) < eps):
                print ".",
            else:
                print "x",

        print "\n"

(L,BD,R) = bidiagonal(A)
print_m(BD)
print "\n\n\n"
print BD
print L*BD*R
print A

