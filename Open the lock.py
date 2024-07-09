def open_lock(key):
    for i in range(4):
        x = int(key[i])
        for d in (-1, 1):
            y = (x + d) % 10
            yield key[:i] + str(y) + key[i+1:]

# Input handling
deadends = input().split(" ")
target = input()

# Convert deadends to a set for quick lookup
dead_set = set(deadends)

# If the initial state is in deadends, return -1 immediately
if '0000' in dead_set:
    print(-1)
else:
    queue = [('0000', 0)]
    visited = {'0000'}
    front = 0
    found = False

    # BFS traversal
    while front < len(queue):
        key, depth = queue[front]
        front += 1
        if key == target:
            print(depth)
            found = True
            break
        for p in open_lock(key):
            if p not in visited and p not in dead_set:
                visited.add(p)
                queue.append((p, depth + 1))

    if not found:
        print(-1)
