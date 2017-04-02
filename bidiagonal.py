import numpy as np;
from householder import *


# PRECOND : A is a n*m numpy float matrix
# Returns Q,BD,R such as Q*BD*R = A
# Q (size n*n) and R (size m*m) orthogonal
# BD (size n*m) upper bidiagonal matrix
def bidiagonal(A,eps=1e-6):
    
    n = A.shape[0]
    m = A.shape[1]

    Qleft = np.matrix(np.eye(n,n))
    Qright = np.matrix(np.eye(m,m))
    BD = A[:]

    for i in range(min(n,m)):

        X = BD[i:n, i]
        
        Y = np.matrix(np.zeros([n-i,1]))
        Y[0,0] = np.linalg.norm(X)

        U1 = np.zeros([n, 1])
        U1[i:n] = calculate_householder_vector(X, Y, eps)
            
        Qleft = optimized_matrix_product_AxH(Qleft, U1)
        BD = optimized_matrix_product_HxA(U1, BD)

        if i < m-2:
            X = BD[i, (i+1):m]
            X = np.transpose(X)
            
            Y = np.matrix(np.zeros([m-i-1,1]))
            Y[0,0] = np.linalg.norm(X)

            U2 = np.zeros([m, 1])
            U2[(i+1):m] = calculate_householder_vector(X, Y, eps)
            
            Qright = optimized_matrix_product_HxA(U2, Qright)
            BD = optimized_matrix_product_AxH(BD, U2)

    return Qleft, BD, Qright

