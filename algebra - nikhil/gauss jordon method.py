def printmat(mat) :
    n = len(mat)
    for i in range(0,n) :
        print(mat[i])
        
mat = [ [2,1,4 ], [1, -1,3], [3,2,5] ]
w = [-9, -7 , -15 ]

n = len(w)

for c in range(0,n) :
    if (mat[c][c]==0):
        print("plz exchange rows...diagonal entry is zero")
    w[c] = w[c] / mat[c][c]
    t = mat[c][c]
    #print("after divistion by:", mat[c][c])
    for r in range(0,n):
        mat[c][r] = mat[c][r] / t
        #print("c & r :", c , ":", r)

    
    #printmat(mat)
                    
    for i in range (0,n) :
        if (i!=c) :            
            w[i] = w[i] - (mat[i][c]*w[c])
            t = mat[i][c]
            for k in range(0,n):
                mat[i][k] = mat[i][k] - ( t * mat[c][k])
    print("after c = ", c)
    printmat(mat)
    print(" w is = ", w)
    
printmat(mat)
print("w is = ")
print(w)
