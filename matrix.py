import random
import numpy as np

eps=1e-10

# Prints shape of matrix A ('.' for a null value, else 'x')
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


# Returns True if matrices A and B are approximately (with an epsilon tolerance) equal
def equal_m(A, B):
    if A.shape != B.shape:
        return false

    eps = 1e-10
    (n,m) = A.shape
    for i in range(n):
        for j in range(m):
            if (A[i,j] - B[i,j]) >= eps:
                return False
    return True


# Generates a matrix A(n,m) where n <= 10 and m <= 10, containing random float numbers between 0 and 20
def generate_matrix():
    n = random.randint(1, 10)
    m = random.randint(1, 10)

    A = np.matrix(np.zeros([n,m]))
    for i in range(n):
        for j in range(m):
            A[i,j] = round(random.uniform(0,10),2)

    return A
