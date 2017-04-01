from householder import *
from scipy.linalg import qr
# Householder tests

X = np.matrix([[3.0], [4.0], [0.0]])
Y = np.matrix([[0.0], [0.0], [5.0]])
n = len(X)
m = random.randint(1,10)
U = calculate_householder_vector(X,Y)
H = householder_vector_to_matrix(U)
optimized_HX = optimized_vector_product(U,X)

print "\nHouseholder vector U:\n", U
print "\nHouseholder Matrix H:\n", H
print "\nOptimized product of H, the Householder matrix of U, and X:\n", optimized_HX


A = np.matrix(np.zeros([n, m]))
for i in range(m):
    A[:,i] = X

print "\nOptimized product of H, the Householder matrix of U, and A a matrix whose ", A.shape[1] ," columns are all equal to X\n", optimized_matrix_product_HxA(U, A)
assert(np.linalg.norm(H*X - Y) < eps)
assert(np.linalg.norm(optimized_vector_product(U,X) - H*X) < eps)

print np.linalg.norm(U)
print U




X = np.array([[1.0],[2.0],[0.0]])
Y = np.array([[0.0],[math.sqrt(5)],[0.]])


A = np.matrix( [[1, 5, 3],
                [3, 6, 4],
                [2, 1, 0]] )


print A
U = calculate_householder_vector(X,Y)
print U
H = householder_vector_to_matrix(U)
print H

print "n"
print optimized_matrix_product_AxH(A,U)
print "\n"
print A*H


print " begin tests\n"
n = random.randint(3,9)
def get_random_ortho_vector(n):
    H = np.random.randn(n, n)
    Q, R = qr(H)
    return Q[:,0].reshape(n,1)
def get_test_vector(n):
    return np.matrix(np.random.randint(4, size=n)).reshape(n,1)
def get_test_matrix(n):
    for i in range(n):
        A[:,i] = get_test_vector(n)
    return A

A = np.matrix(np.zeros([n,n]))
nb_tests = 668
for i in range(nb_tests):
    A = get_test_matrix(n)
    U = get_random_ortho_vector(n)
    H = householder_vector_to_matrix(U)
    print "\t\tRandom Householder Matrix H:\n",H
    optimized_HA = optimized_matrix_product_HxA(U,A)
    optimized_AH = optimized_matrix_product_AxH(A,U)
    AH = A*H
    HA = H*A
    assert(np.linalg.norm(optimized_AH - AH) < eps)
    assert(np.linalg.norm(optimized_HA - HA) < eps)
    print "\n\n\t\tOptimized product A*H\n",optimized_AH
    print "\n\n\t\tRegular product A*H\n", AH
    print "\n\n\t\tOptimized product H*A\n",optimized_HA
    print "\n\n\t\tRegular product H*A\n", HA
    print " \n\n\n\t\t\tTest number:",nb_tests," Passed\n\n"


print "\n\n\n\t\t\t\tEnd of tests\n"
