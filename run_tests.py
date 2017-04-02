from tests import *
from compression import *




#tests

test_optimized_matrix_product()

test_bidiagonal()

test_low_to_up_bidiag_qr()

test_decomp_svd()

test_conv_S()


# Image compression example

print "Compression of the picture: "
display_compressed_image("lena.jpg",25)
