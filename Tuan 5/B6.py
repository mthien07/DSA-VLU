#02134
import sys
def dijkstra_early_exit(adj,s,t):
    n = len(adj)
    dist = [sys.maxsize] * n
    dist[s] = 0
    visited = [False] * n
    for _ in range(n):
        min_d = sys.maxsize
        u = -1
        for i in range(n):
            if not visited[i] and dist[i] < min_d:
                min_d = dist[i]
                u = i
        if u == -1:
            break
        if u == t:
            break
        visited[u] = True
        for v,weight in adj[u]:
            if not visited[v] and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
    return dist