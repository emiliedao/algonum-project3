from bidiagonal import *
from print_matrix import *

# Tests

# to do : generate random matrix
A = np.matrix( [[1, 5],
                [3, 6],
                [2, 1]] )

(L,BD,R) = bidiagonal(A)
print_m(BD)
print "\n\n\n"
print BD
print L*BD*R
