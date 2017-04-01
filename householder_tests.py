from householder import *
from scipy.linalg import qr
# Householder tests


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


nb_tests = 658
print "\t\t\t Begin tests:\n\n"
for i in range(nb_tests):
    n = random.randint(3,9)
    A = np.matrix(np.zeros([n,n]))
    A = get_test_matrix(n)
    U = get_random_ortho_vector(n)
    H = householder_vector_to_matrix(U)
    optimized_HA = optimized_matrix_product_HxA(U,A)
    optimized_AH = optimized_matrix_product_AxH(A,U)
    AH = regular_product_AxH(A,H)
    HA = regular_product_HxA(H,A)
    assert(np.linalg.norm(optimized_AH - AH) < eps)
    assert(np.linalg.norm(optimized_HA - HA) < eps)
    print "\t\tRandom Householder Matrix H:\n",H
    print "\n\n\t\tOptimized product A*H\n",optimized_AH
    print "\n\n\t\tRegular product A*H\n", AH
    print "\n\n\t\tOptimized product H*A\n",optimized_HA
    print "\n\n\t\tRegular product H*A\n", HA
    print " \n\n\n\t\t\tTest number ",nb_tests,": Passed\n\n"


print "\n\n\n\t\t\t\tEnd of tests\n"
