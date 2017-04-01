from bidiagonal import *
from matrix import *
from svd import *

#
# Each test generates and test nb_tests random matrix. It returns the 
# proportion of passed tests.
#

def test_bidiagonal(nb_tests=100,eps=1e-6):

    nb_passed = 0
    
    for i in range(nb_tests):
        
        A = generate_matrix()
        (L,BD,R) = bidiagonal(A,eps)
        
        if (is_bidiagonal(BD,eps) and equal_m(L*BD*R,A,eps)):
            nb_passed += 1

    print "Test of bidiagonal() : ",nb_passed,"/",nb_tests," passed tests."
    return float(nb_passed)/float(nb_tests)




def test_low_to_up_bidiag_qr(nb_tests=100,eps=1e-6):

    nb_passed = 0
    
    for i in range(nb_tests):
        
        A = rand_low_bidiag()
        Q,BD = low_to_up_bidiag_qr(A,eps)
        if (is_bidiagonal(BD) and equal_m(Q*BD,A)):
            nb_passed += 1

    print "Test of low_to_up_bidiag_qr() : ",nb_passed,"/",nb_tests," passed tests."
    return float(nb_passed)/float(nb_tests)




def test_decomp_svd(nb_tests=100,nb_iter_svd=100,eps=1e-6):

    nb_passed = 0
    
    for i in range(nb_tests):

        BD = rand_up_bidiag()
        (U,S,V) = decomp_svd(BD,nb_iter_svd,eps)

        if (equal_m(U*S*V,BD,eps) and is_diagonal(S,eps)):
            nb_passed += 1
    
    print "Test of decomp_svd() : ",nb_passed,"/",nb_tests," passed tests."
    return float(nb_passed)/float(nb_tests)










