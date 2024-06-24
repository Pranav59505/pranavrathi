m,n = map(int,input().split())

# Read the m*n matrix
grid = []
for _ in range(m):
    row = list(map(int, input().split()))
    grid.append(row)
def rottening(m,n,grid):
    minute=0
    count=0
    for i in range(m):
        for j in range(n):
            if grid[i][j]!=0 and grid[i][j]==2:
                if i+1<m:
                    if grid[i+1][j]==1:
                        grid[i+1][j]=2
                        count=count+1
                if i-1<m and i-1>=0:
                    if grid[i-1][j]==1:
                        grid[i-1][j]=2
                        count=count+1
                if j+1<n:
                    if grid[i][j+1]==1:
                        grid[i][j+1]=2
                        count=count+1
                if j-1<n and j-1>=0:
                    if grid[i][j-1]==1:
                        grid[i][j-1]=2
                        count=count+1
                if(count>0):
                    minute=minute+1
                    count=0
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1:
                return -1
    return minute
print(rottening(m,n,grid))
