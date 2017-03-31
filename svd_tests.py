from svd import *
from bidiagonal import *
from print_matrix import *

# SVD tests
A = np.matrix( [[1, 5, 4, 3, 3],
                [3, 6, 5, 0, 2],
                [2, 1, 4, 9, 3]] )

(L,BD,R) = bidiagonal(A)
(U, S, V) = decomp_svd(BD)
print_m(U)
print_m(V)
print_m(BD)
print_m(S)
