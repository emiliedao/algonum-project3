import numpy as np
from matrix import *
from bidiagonal import *

# Single Value Decomposition algorithm  : applies nmax times the QR decomposition on BD (numpy version)
# Precond : BD is bidiagonal
# Postcond : S converges to a diagonal matrix
def decomp_svd(BD):
    n = BD.shape[0]
    m = BD.shape[1]
    U = np.matrix(np.eye(n, n))
    V = np.matrix(np.eye(m, m))
    S = BD

    nmax = 10
    for i in range(nmax):
        Q1, R1 = np.linalg.qr(np.transpose(S))
        Q2, R2 = np.linalg.qr(np.transpose(R1))
        S = R2
        U = U * Q2
        V = np.transpose(Q1) * V

        # print "R1"
        # print R1
        # print_m(R1)
        #
        # print "R2"
        # print R2
        # print_m(R2)
        #
        # print "S"
        # print S
        # print_m(S)
        # assert(is_bidiagonal(R1))
        # assert(is_bidiagonal(R2))
        # assert(is_bidiagonal(S))
        assert(equal_m(U*S*V,BD))
    return U, S, V
