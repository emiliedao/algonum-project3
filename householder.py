import numpy as np;

def calculate_U(X, Y, eps=1e-10):
    n = X.size
    U = np.matrix(np.zeros([n,1]))

    norm = np.linalg.norm(X - Y)

    # X != Y
    if norm > eps:
        U = np.dot(1/norm, X - Y)

    return U


def calculate_householder(U):
    n = U.size
    return np.matrix(np.eye(n,n)) - 2*U*np.transpose(U)


def calculate_optimized_householder(U, X):
    lbda = np.transpose(X)*U
    return X - 2*lbda[0,0]*U


def householder(X, Y):
    return calculate_householder(calculate_U(X, Y))


# Builds the matrix [ [Id, 0], [0, H] ] of size n
#def reshape_householder(H, n):
#    A = np.eye(H.size/2,


##################################
# Tests

X = np.matrix([3.0, 4, 0]) .T
Y = np.matrix([0, 0, 5]) .T

U = np.matrix(calculate_U(X, Y))
print "Matrix U :\n", U

H = calculate_householder(U)
print "\nHouseholder :\n", H

V = np.matrix([1,0,0]) . T
S = calculate_optimized_householder(U, V)
print "\nOptimized Householder :\n", S
