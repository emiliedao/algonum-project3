eps=1e-10

# Matrix pretty print
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
