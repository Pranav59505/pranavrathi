n, m = map(int, input().split())

# adjacency list for undirected graph
# time complexity: O(2E)
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

X=[1]
# You can print adj or do something else with it
def search(x):
    for i in adj[x]:
        if i not in X:
            X.append(i)
            search(i)
search(1)
print(X)
