from bidiagonal import *

# Tests

# to do : generate random matrix
A = np.matrix( [[1, 5],
                [3, 6],
                [2, 1]] )

# Matrix pretty print
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
