import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import ceil



def transf_mat(A,color):

    (height,width) = np.shape(A)

    M = [np.array([np.array([256,256,256]) for j in range(width)]) for i in range(height)]
         
    for i in range(height):
        for j in range(width):
            M[i][j][color] -= ceil(A[i,j])
            
    return np.array(M)


#color : 0(red) 1(green) 2(blue)
def compression(path,k,color):

    img = Image.open(path)
    (width,height) = img.size
    #img.show()
    A = np.matrix(np.zeros([height,width]))

    for i in range(height):
        for j in range(width):
            pix = (img.getpixel((j,i))[color])
            A[i,j] = pix


    (U,s,V) = np.linalg.svd(A,full_matrices=False)
    S = np.matrix(np.diag(s))

    for i in range(k,min(height,width)):
        S[i,i] = 0.

    A_new = U*S*V 
    
    return transf_mat(A_new,color)

k = 50
path = "lena.jpg"
Im_red = compression(path,k,0)
Im_green = compression(path,k,1)
Im_blue = compression(path,k,2)



plt.imshow(Im_red + Im_green + Im_blue)
plt.show()
