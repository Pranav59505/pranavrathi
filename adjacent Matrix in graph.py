n, m = map(int, input().split())
# adjacency matrix for undirected graph
# time complexity: O(n)
adj = [[0] * (n + 1) for _ in range(n + 1)]
visited=[]
X=[]
Y=[]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u][v] = 1
    adj[v][u] = 1  # this statement will be removed in case of directed graph
for rows in range(len(adj)):
    print(adj[rows])