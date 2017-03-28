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
    return np.matrix(np.eye(len(U), len(U)) - 2*U*np.transpose(U))

def optimized_vector_product(U,X):
    assert(len(U) == len(X))
    assert((np.linalg.norm(U) - 1.0)<eps)

    return X - 2*U*np.transpose(U)*X


def optimized_matrix_product_HxA(U,A):
    assert(len(U) == len(A))
    assert((np.linalg.norm(U) - 1.0)<eps)

    product_result = np.matrix(np.zeros([len(U), A.shape[1]]))
    for i in range(A.shape[1]):
            product_result[:, i] = optimized_vector_product(U,A[:, i])
    return product_result


def optimized_matrix_product_AxH(A,U):
    n = len(A)
    m = len(U)
    print n
    print m
    print A.shape[1]
    assert(m == A.shape[1])
    assert((np.linalg.norm(U) - 1.0)<eps)

    product_result = np.matrix(np.zeros([n,m]))
    for i in range(m):
        v = optimized_vector_product(U,np.reshape(A[i, :],[n,1]))
        product_result[i, : ] = np.reshape(v,[1,n])
    return product_result






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
