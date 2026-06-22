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

def dijkstra_qua_dinh_bat_buoc(adj, s, t, k):
    dist_s = dijkstra(adj, s)
    dist_k = dijkstra(adj, k)
    if dist_s[k] == sys.maxsize or dist_k[t] == sys.maxsize:
        return sys.maxsize
    return dist_s[k] + dist_k[t]
