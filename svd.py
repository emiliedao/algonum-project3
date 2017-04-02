import numpy as np
from bidiagonal import *




# Single Value Decomposition algorithm  : applies nmax times the QR decomposition on BD (numpy version)
# Precond : BD is bidiagonal
# Postcond : S converges to a diagonal matrix
def decomp_svd(BD,nmax=50,eps=1e-6):
    
    n = BD.shape[0]
    m = BD.shape[1]
    U = np.matrix(np.eye(n, n))
    V = np.matrix(np.eye(m, m))
    S = BD[:]

    for i in range(nmax):
    
        Q1, R1 = low_to_up_bidiag_qr(np.transpose(S),eps)
        Q2, R2 = low_to_up_bidiag_qr(np.transpose(R1),eps)

        S = R2
        U = U * Q2
        V = np.transpose(Q1) * V

    sort_diag(U,S,V)
    make_positive_diag(U,S)
        
    return U, S, V




# PRECOND : A is a lower bidiagonal n*m matrix
# Returns Q,BD such as Q*BD = A
# Q : n*n orthogonal matrix
# BD : n*m upper bidiagonal matrix
def low_to_up_bidiag_qr(A,eps=1e-6):

    n = A.shape[0]
    m = A.shape[1]
    Q = np.matrix(np.eye(n,n))
    BD = A[:]
    
    for i in range(min(n,m)):
        
        X = BD[i:n, i]

        Y = np.matrix(np.zeros([n-i,1]))
        Y[0,0] = np.linalg.norm(X)
        
        U1 = np.zeros([n, 1])
        U1[i:n] = calculate_householder_vector(X, Y, eps)
        
        Q = optimized_matrix_product_AxH(Q, U1)
        BD = optimized_matrix_product_HxA(U1, BD)
        
    return Q,BD


# PRECOND : S diagonal matrix, U*S*V = A
# Modifies U,S and V such as S is sorted
# and U*S*V = A
def sort_diag(U,S,V):

    (n,m) = S.shape

    pivot = 0

    for pivot in range(min(n,m)):

        ind_max = pivot
        max_val = abs(S[pivot,pivot])
        
        for i in range(pivot+1,min(n,m)):

            if abs(S[i,i]) > max_val:
                ind_max = i
                max_val = abs(S[i,i])
                
        switch_lines(S,ind_max,pivot)
        switch_columns(S,ind_max,pivot)
        
        switch_columns(U,ind_max,pivot)
        switch_lines(V,ind_max,pivot)


        
#PRECOND : S diagonal matrix, U*S = A
# Modifies U and S such as S has only
# positives numbers and U*S = A 
def make_positive_diag(U,S):

    (n,m) = S.shape

    for i in range(min(n,m)):

        if S[i,i] < 0:
            S[i,:] = - S[i,:]
            U[:,i] = - U[:,i]

            

def switch_lines(A,i,j):

    (n,m) = A.shape
    
    if i == j or i >= n or j >= n:
        return

    C = np.copy(A[i,:])

    for k in range(m):
        A[i,k] = A[j,k]
        A[j,k] = C[0,k]



def switch_columns(A,i,j):

    (n,m) = A.shape
    
    if i == j or i >= m or j >= m:
        return

    C = np.copy(A[:,i])

    for k in range(n):
        A[k,i] = A[k,j]
        A[k,j] = C[k,0]




