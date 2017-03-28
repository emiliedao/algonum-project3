from householder import *

#tests
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
for i in range(n+1):
    A[:,i] = X
print "\nOptimized product of H, the Householder matrix of U, and A a matrix whose ", A.shape[1] ," columns are all equal to X\n", optmized_matrix_product(U, A)
assert(np.linalg.norm(H*X - Y) < eps)
assert(np.linalg.norm(optimized_vector_product(U,X) - H*X) < eps)



print np.linalg.norm(U)
print U
