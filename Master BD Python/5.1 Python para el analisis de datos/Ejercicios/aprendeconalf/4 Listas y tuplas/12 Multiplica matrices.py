A=[[1,2,3],[4,5,6]]
B= [[-1,0],[0,1],[1,1]]

def multiplica_matrices(A,B):

    if len(A[0])!=len(B):
        return "No se pueden multiplicar"
    else:
        C=[]
        for i in range(len(A)):
            C.append([])
            for j in range(len(B[0])):
                C[i].append(0)
                for k in range(len(B)):
                    C[i][j] += A[i][k]*B[k][j]

        return C


print(multiplica_matrices(A,B))