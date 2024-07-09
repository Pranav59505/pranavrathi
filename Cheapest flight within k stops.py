def find_cheapest_price(n, flights, src, dst, k):
    # Initialize distances array with inf, except for the starting point
    distances = [float('inf')] * n
    distances[src] = 0

    # Iterate k + 1 times (0 stops to k stops)
    for i in range(k + 1):
        # Make a copy of the distances to use for updates
        new_distances = distances[:]
        # Relax edges
        for u, v, price in flights:
            if distances[u] == float('inf'):
                continue
            new_distances[v] = min(new_distances[v], distances[u] + price)
        # Update distances
        distances = new_distances

    return -1 if distances[dst] == float('inf') else distances[dst]

n = int(input())
flights = [input()]
src = input()
dst = input()
k = input()
print(find_cheapest_price(n, flights, src, dst, k))  # Output: 200
