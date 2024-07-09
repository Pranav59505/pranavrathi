m,n=map(int,input().split())
M=[]
for i in range(m):
    x=map(str,input())
    y=list(x)
    for j in range(n-1):
        y.remove(' ')
    M.append(y)
Y=[]
def replacement(M,i,j):
    global Y
    if(M[i][j]=='o'):
        for k in range(i):
            if(M[k][j]=='x'):
                Y.append(0)
        for k in range(i,m):
            if (M[k][j] == 'x'):
                Y.append(1)
        for k in range(j):
            if (M[i][k] == 'x'):
                Y.append(2)
        for k in range(j, n):
            if (M[i][k] == 'x'):
                Y.append(3)

P=[]

for i in range(m):
    for j in range(n):
        replacement(M,i,j)
        for _ in Y:
            if _ not in P:
                P.append(_)
        if(len(P)==4):
            M[i][j]='x'
        Y.clear()
        P.clear()
for rows in M:
    print(rows)

