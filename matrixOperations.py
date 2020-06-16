def add(A,B):
    C = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(0,len(A)):
        for j in range(0,len(A[0])):
            C[i][j] = A[i][j] + B[i][j]
    return C

def multiply (A,B):
    C = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C

if (__name__=="__main__"):
    m,n=3,3
    A = [[1,1,1],[2,2,2],[3,3,3]]
    B = [[3,3,3],[2,2,2],[1,1,1]]
    C = add(A,B)
    D = multiply(A,B)
    print(C)