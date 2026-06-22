import sys

def dijkstra_dem(adj, s):
    n = len(adj)
    dist = [sys.maxsize] * n
    count = [0] * n
    dist[s] = 0
    count[s] = 1
    visited = [False] * n

    for _ in range (n):
        min_d = sys.maxsize
        u = -1
        for i in range (n):
            if not visited[i] and dist[i] < min_d:
                min_d = dist[i]
                u = i
        if u == -1:
            break
        visited[u] = True
        for v, weight in adj[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                count[v] = count[u]
            elif dist[u] + weight == dist[v]:
                count[v] += count[u]
    return dist, count
