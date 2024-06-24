n, m = map(int, input().split())

# adjacency list for undirected graph
# time complexity: O(2E)
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

X=[1]
Y=[]
# You can print adj or do something else with it
def search(x):
    for i in adj[x]:
        if i not in X:
            X.append(i)
            search(i)
for i in range(1,n+1):
    search(i)
    Y.append(int(len(X)))
    X.clear()
def count(x,Y):
    m=0
    for i in Y:
        if i==x:
            m=m+1
    return m
answer=0
for i in range(1,m+1):
    answer=answer+count(i,Y)/i
print(answer)
