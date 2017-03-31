from bidiagonal import *
from matrix import *

A = generate_matrix()

(L,BD,R) = bidiagonal(A)

print_m(BD)
assert(is_bidiagonal(BD))
assert(equal_m(L*BD*R, A))
