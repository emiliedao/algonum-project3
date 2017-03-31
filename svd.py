import numpy as np

# Single Value Decomposition algorithm  : applies nmax times the QR decomposition on BD (numpy version)
# Precond : BD is bidiagonal
# Postcond : S converges to a diagonal matrix
def decomp_svd(BD):
    n = BD.shape[0]
    m = BD.shape[1]
    U = np.matrix(np.eye(n, n))
    V = np.matrix(np.eye(m, m))
    S = BD

    nmax = 100
    for i in range(nmax):
        Q1, R1 = np.linalg.qr(np.transpose(S))
        Q2, R2 = np.linalg.qr(np.transpose(R1))
        S = R2
        U = U * Q2
        V = np.transpose(Q1) * V

        # TODO : write a function which testes equality
        #assert(U*S*V == BD)
    return U, S, V


