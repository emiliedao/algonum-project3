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
    n = A.shape[0]
    m = A.shape[1]
    assert((np.linalg.norm(U) - 1.0)<eps)

    product_result = np.matrix(np.zeros([n,m]))
    print product_result
    for i in range(n):
        print A[i,:]
       # v = optimized_vector_product(U,A[i, :].reshape([m,1])))
        #print shape(v)
        
        #product_result[i] = v.reshape([1,m])
    return product_result




