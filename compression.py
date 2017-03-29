import numpy as np
from PIL import Image


def f(path):

    img = Image.open(path)
    (width,height) = img.size
    #img.show()
    A = np.matrix(np.zeros([height,width]))

    for i in range(height):
        for j in range(width):
            A[i,j] = (img.getpixel((j,i)))[0]

    print A
    (U,s,V) = np.linalg.svd(A,full_matrices=False)
    S = np.matrix(np.diag(s))
    print U
    print S
    print V



f("plant.jpg")
