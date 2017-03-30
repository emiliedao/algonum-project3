from householder import *

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
