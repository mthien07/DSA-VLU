import sys

def dijkstra(adj, s):
    n = len(adj)
    dist = [sys.maxsize] * n
    dist[s] = 0
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
            if not visited[v] and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
 
    return dist

def dijkstra_nhieu_truy_van(adj, queries):
    nguon_set = set()
    for s, t in queries:
        nguon_set.add(s)

    cache = {}
    for s in nguon_set:
        cache[s] = dijkstra(adj, s)

    results = []
    for s, t in queries:
        results.append(cache[s][t])
    return results
