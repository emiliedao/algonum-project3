import numpy as np

# Algorithme de décomposition SVD : applique n fois la transformation QR (version numpy) sur la matrice bidiagonale BD
# Precond : BD est bidiagonale
# Postcond : S converge vers une matrice diagonale
def decomp_svd(BD):
    n = len(BD)
    U = np.eye(n, n)
    V = np.eye(n, n)
    S = BD

    for i in range(n):
        Q1, R1 = np.linalg.qr(np.transpose(S))
        Q2, R2 = np.linalg.qr(np.tranpose(R1))
        S = R2
        U = U * Q2
        V = np.tranpose(Q1) * V

        print "S\n", S
        assert(U*S*V == BD)
    return U, S, V
