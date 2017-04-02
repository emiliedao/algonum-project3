from bidiagonal import *
from matrix import *
from svd import *


# Display the nb_tests A*H and H*A matrix
# obtained 
def test_optimized_matrix_product(nb_tests=100,eps=1e-10):
    
    print "\t\t\t Optimized products : Begin tests:\n\n"
    for i in range(nb_tests):
        n = random.randint(3,9)
        A = np.matrix(np.random.rand(n,n))
        U = get_random_ortho_vector(n)
        H = householder_vector_to_matrix(U)
        optimized_HA = optimized_matrix_product_HxA(U,A)
        optimized_AH = optimized_matrix_product_AxH(A,U)
        AH = A*H
        HA = H*A
        assert(np.linalg.norm(optimized_AH - AH) < eps)
        assert(np.linalg.norm(optimized_HA - HA) < eps)
        print "\t\tRandom Householder Matrix H:\n",H
        print "\n\n\t\tOptimized product A*H\n",optimized_AH
        print "\n\n\t\tRegular product A*H\n", AH
        print "\n\n\t\tOptimized product H*A\n",optimized_HA
        print "\n\n\t\tRegular product H*A\n", HA
    
    print " \n\n\n\t\t\tTest number ",nb_tests,": Passed\n\n"

    

#
# Each one of these three tests generates and test nb_tests random matrix. It returns
# and displays the proportion of passed tests.
#

def test_bidiagonal(nb_tests=1000,eps=1e-10):
    
    print "Test of bidiagonal() : ",
    
    nb_passed = 0
    
    for i in range(nb_tests):
        
        A = generate_matrix()
        (L,BD,R) = bidiagonal(A,eps)
        
        if (is_bidiagonal(BD,eps) and equal_m(L*BD*R,A,eps)):
            nb_passed += 1

    print nb_passed,"/",nb_tests," passed tests."
    return float(nb_passed)/float(nb_tests)




def test_low_to_up_bidiag_qr(nb_tests=1000,eps=1e-10):

    print "Test of low_to_up_bidiag_qr() : ",
    
    nb_passed = 0
    
    for i in range(nb_tests):
        
        A = rand_low_bidiag()
        Q,BD = low_to_up_bidiag_qr(A,eps)
        if (is_bidiagonal(BD,eps) and equal_m(Q*BD,A,eps)):
            nb_passed += 1

    print nb_passed,"/",nb_tests," passed tests."
    return float(nb_passed)/float(nb_tests)




def test_decomp_svd(nb_tests=50,nb_iter_svd=200,eps=1e-6):

    print "Test of decomp_svd() : "
    
    passed_prod = 0
    passed_diag = 0
    
    for i in range(nb_tests):

        BD = rand_up_bidiag()
        (U,S,V) = decomp_svd(BD,nb_iter_svd,eps)

        if equal_m(U*S*V,BD,eps):
            passed_prod +=1

        if is_diagonal(S,eps):
            passed_diag += 1
    
    print "Product still the same : ",passed_prod,"/",nb_tests," passed tests."
    print "S diagonal : ",passed_diag,"/",nb_tests," passed tests."
    return float(min(passed_diag,passed_prod))/float(nb_tests)



# Displays series of histograms representing the
# matrix S becoming diagonal during svd transformation
def test_conv_S(nmax=50,disp_freq=10,eps=1e-6):

    BD = rand_up_bidiag()
    
    n = BD.shape[0]
    m = BD.shape[1]
    U = np.matrix(np.eye(n, n))
    V = np.matrix(np.eye(m, m))
    S = BD[:]

    for i in range(nmax):
    
        Q1, R1 = low_to_up_bidiag_qr(np.transpose(S),eps)
        Q2, R2 = low_to_up_bidiag_qr(np.transpose(R1),eps)

        S = R2
        
        if i%disp_freq == 0:
            histo_mat(S)
            
        U = U * Q2
        V = np.transpose(Q1) * V



