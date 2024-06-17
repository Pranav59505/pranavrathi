import math
from collections import deque

n = int(input())
m = map(int, input().split())
s, t = map(int, input().split())
X = []
Y = []
for i in m:
    X.append(i)
for i in range(len(X)):
    for j in range(i):
        if (math.gcd(X[i], X[j]) != 1):
            Y.append([j + 1, i + 1])
# print(Y)
adj = [[] for _ in range(n + 1)]
for i in range(len(Y)):
    [u, v] = Y[i]
    adj[u].append(v)
    adj[v].append(u)


# print(adj)


def min_path(adj, start, end):
    if start == end:
        return 0
    else:
        # Initialize the visited list
        visited = [False] * len(adj)

        # Distance array to store the minimum distance from start node
        distance = [float('inf')] * len(adj)

        # Queue for BFS
        queue = deque([start])

        # Mark the start node as visited and set distance to 0
        visited[start] = True
        distance[start] = 0

        while queue:
            # Dequeue a vertex from queue
            node = queue.popleft()

            # Get all adjacent vertices of the dequeued vertex
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    print(neighbor, end=" ")
                    # Update distance
                    distance[neighbor] = distance[node] + 1

                    # If we reach the end node, return the distance
                    if neighbor == end:
                        print()
                        return distance[end]

        # If the end node is not reachable, return -1 or any indication of no path
        return -1

print(min_path(adj, s, t) + 1)
