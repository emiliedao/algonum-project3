import random
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt



# Prints shape of matrix A ('.' for a null value, else 'x')
def print_m(A,eps=1e-6):
    
    (n,m) = A.shape
    print "\n"
    
    for i in range(n):
        for j in range(m):

            if (abs(A[i,j]) < eps):
                print ".",
            else:
                print "x",

        print "\n"


# Displays an histogram of the absolute values of the matrix M
def histo_mat(M):

    (n,m) = M.shape

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    xpos = []
    ypos = []
    zpos = [0 for i in range(n*m)]

    dx = [0.5 for j in range(n*m)]
    dy = [0.5 for i in range(n*m)]
    dz = []
    
    for i in range(n):
        for j in range(m):
            xpos.append(j)
            ypos.append(i)
            dz.append(abs(M[i,j]))


    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='r', zsort='average')
    plt.xlabel("i")
    plt.ylabel ("j")
    plt.show()


# Returns True if matrices A and B are approximately (with an epsilon tolerance) equal
def equal_m(A, B, eps=1e-6):

    (n,m) = A.shape
    
    if B.shape != (n,m):
        return false

    for i in range(n):
        for j in range(m):
            if abs(A[i,j] - B[i,j]) >= eps:
                return False
            
    return True


# Returns True if A is (upper) bidiagonal
def is_bidiagonal(A, eps=1e-6):
    
    (n,m) = A.shape
    
    for i in range(n):
        for j in range(m):
    
            if (j != i and j != i+1 and abs(A[i,j]) > eps):
                    return False
                
    return True


def is_diagonal(A,eps=1e-6):

    (n,m) = A.shape

    for i in range(n):
        for j in range(m):

            if i != j and abs(A[i,j] >= eps):
                return False
            
    return True



# Generates a random vector of norm 1 and dimension n
def get_random_ortho_vector(n):

    U = np.matrix(np.random.rand(n,1))
    U = U/np.linalg.norm(U)
    
    return U
    

# Generates a matrix A(n,m) where n < 10 and m < 10, containing random float numbers between 0 and 10
def generate_matrix():
    n = random.randint(1, 10)
    m = random.randint(1, 10)

    A = np.matrix(np.zeros([n,m]))
    for i in range(n):
        for j in range(m):
            A[i,j] = round(random.uniform(0,10),2)

    return A


# Generates random low bidiagonal matrix
def rand_low_bidiag():
    
    n = random.randint(1, 10)
    m = random.randint(1, 10)
    A = np.matrix(np.zeros([n,m]))
    
    for i in range(min(n,m)):

        A[i,i] = round(random.uniform(0,10),2)

        if i+1 < n:
            A[i+1,i] = round(random.uniform(0,10),2)
            
    return A

# Generates random upper bidiagonal matrix
def rand_up_bidiag():
    
    n = random.randint(5, 20)
    m = random.randint(5, 20)
    A = np.matrix(np.zeros([n,m]))
    
    for i in range(min(n,m)):

        A[i,i] = round(random.uniform(0,10),2)

        if i+1 < m:
            A[i,i+1] = round(random.uniform(0,10),2)
            
    return A


