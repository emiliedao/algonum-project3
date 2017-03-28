import numpy as np;
import random;
import math;
eps=1e-10
def calculate_householder_vector(X, Y):
    assert(len(X) == len(Y))
    n = len(X)
    U = np.matrix(np.zeros([n,1]))
    norm = np.linalg.norm(X - Y)
    # X != Y
    if norm > eps:
        U = np.dot(1/norm, X - Y)
    assert((np.linalg.norm(U) - 1.0)<eps)
    return U
def householder_vector_to_matrix(U):
    return np.matrix(np.eye(n,n)) - 2*U*np.transpose(U)

def optimized_vector_product(U,X):
    assert(len(U) == len(X))
    assert((np.linalg.norm(U) - 1.0)<eps)

    return X - 2*U*np.transpose(U)*X


def optmized_matrix_product(U,A):
    assert(len(U) == len(A))
    assert((np.linalg.norm(U) - 1.0)<eps)

    product_result = np.matrix(np.zeros([len(U), A.shape[1]]))
    for i in range(A.shape[1]):
            product_result[:, i] = optimized_vector_product(U,A[:, i])
    return product_result
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
