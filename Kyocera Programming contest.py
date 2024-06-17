from collections import deque


def min_path(adj, start, end):
   if start==end:
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
                # Update distance
                distance[neighbor] = distance[node] + 1

                # If we reach the end node, return the distance
                if neighbor == end:
                    return distance[end]

    # If the end node is not reachable, return -1 or any indication of no path
    return -1


n, m ,k = map(int, input().split())

# adjacency list for undirected graph
adj = [[] for _ in range(n + 1)]
guarded=[False]*len(adj)
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
for _ in range(k):
    p,h = map(int, input().split())
    for i in range(1,len(adj)):
        #print(min_path(adj,p,i))
        if(min_path(adj,p,i)<=h and min_path(adj,p,i)>=0):
            guarded[i]=True

X=[]
for i in range(len(guarded)):
    if guarded[i]==True:
        X.append(i)
print(len(X))
for i in range(len(guarded)):
    if guarded[i] == True:
        print(i,end=" ")

