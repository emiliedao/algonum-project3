import numpy as np;
import random;
import math;



def calculate_householder_vector(X, Y, eps=1e-6):
    
    n = len(X)
    U = np.matrix(np.zeros([n,1]))
    norm = np.linalg.norm(X - Y)
    
    if norm > eps:
        U = np.dot(1/norm, X - Y)
        
    return U


        
def householder_vector_to_matrix(U):
    
    n = len(U)
    return np.matrix(np.eye(n,n) - 2*U*np.transpose(U))



def optimized_vector_product(U,X):
        
    return X - 2*U*np.transpose(U)*X



def optimized_matrix_product_HxA(U,A):
        
    return A - 2*U*(U.transpose()*A)



def optimized_matrix_product_AxH(A,U):
            
    return A - 2*(A*U)*(U.transpose())
