m, n = map(int, input().split())

# Read the m*n matrix
grid = []
for _ in range(m):
    row = list(map(int, input().split()))
    grid.append(row)
sr = int(input())
sc = int(input())
new_color = int(input())
x = grid[sr][sc]


def filling(m, n, sr, sc, new_color, grid):
    global x
    if sr + 1 < m:
        if grid[sr + 1][sc] == x:
            grid[sr + 1][sc] = new_color
            filling(m, n, sr + 1, sc, new_color, grid)
    if sr - 1 >= 0:
        if grid[sr - 1][sc] == x:
            grid[sr - 1][sc] = new_color
            filling(m, n, sr - 1, sc, new_color, grid)
    if sc + 1 < n:
        if grid[sr][sc + 1] == x:
            grid[sr][sc + 1] = new_color
            filling(m, n, sr, sc + 1, new_color, grid)
    if sc - 1 >= 0:
        if grid[sr][sc - 1] == x:
            grid[sr][sc - 1] = new_color
            filling(m, n, sr, sc - 1, new_color, grid)


filling(m, n, sr, sc, new_color, grid)
for row in grid:
    print(row)
