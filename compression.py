import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import ceil
from svd import *


        
# Given the path to an image, displays the
# SVD compression at rank k
def display_compressed_image(path,k):

    (U_red,S_red,V_red) = image_to_USV(path,0)
    (U_green,S_green,V_green) = image_to_USV(path,1)
    (U_blue,S_blue,V_blue) = image_to_USV(path,2)

    (n,m) = S_red.shape

    for i in range(k+1,min(n,m)):
        S_red[i,i] = 0.
        S_green[i,i] = 0.
        S_blue[i,i] = 0.

    M_red = U_red*S_red*V_red
    M_green = U_green*S_green*V_green
    M_blue = U_blue*S_blue*V_blue
    
    img_red = matrix_to_image(M_red,0)
    img_green = matrix_to_image(M_green,1)
    img_blue = matrix_to_image(M_blue,2)

    img = img_red + img_green + img_blue 

    plt.imshow(img)
    plt.show()
    


# Returns the USV decomposition of the image
# given with "path" for the color given (0 for red,
# 1 for green, 2 for blue)
def image_to_USV(path,color):

    img = Image.open(path)
    (width,height) = img.size
    A = np.matrix(np.zeros([height,width]))

    for i in range(height):
        for j in range(width):
            pix = (img.getpixel((j,i))[color])
            A[i,j] = pix


    (Qleft,BD,Qright) = bidiagonal(A)
    (U,S,V) = decomp_svd(BD)

    # S may not be exactly  diagonal : suppression of the
    # residual information outside the diagonal
    for i in range(height):
        for j in range(width):
            if i != j:
                A[i,j] = 0.

    return (Qleft*U,S,V*Qright)



# Create a displayable (with plt.imshow()) image from the
# float matrix A with the color given (0 for red,
# 1 for green, 2 for blue).
def matrix_to_image(A,color):

    (height,width) = np.shape(A)

    M = [np.array([np.array([256,256,256]) for j in range(width)]) for i in range(height)]
         
    for i in range(height):
        for j in range(width):
            M[i][j][color] -= ceil(A[i,j])
            
    return np.array(M)




    
