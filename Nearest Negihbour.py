m,n=map(int,input().split())
M=[]
for i in range(n):
    x=map(int,input().split())
    y=list(x)
    M.append(y)
def check(M,x,y):
    return 0
def nearest_neighbour(M,i,j):
    if M[i][j]==1:
        return 0
    if M[i][j]!=1:
        for k in range(1,m):
            if i+k<m:
                if M[i+k][j]==1:
                    return k
            if i-k>=0:
                if M[i-k][j]==1:
                    return k
            if j+k<m:
                if M[i][j+k]==1:
                    return k
            if j-k>=0:
                if M[i][j-k]==1:
                    return k
result=[[] for i in range(n)]
for i in range(m):
    for j in range(n):
        result[i].append(nearest_neighbour(M,i,j))
for rows in result:
    print(rows)
