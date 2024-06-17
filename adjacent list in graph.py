n, m = map(int, input().split())

# adjacency list for undirected graph
# time complexity: O(2E)
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# You can print adj or do something else with it
for i in range(len(adj)):
    print(f"{i}: {adj[i]}")
