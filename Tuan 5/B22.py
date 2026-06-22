import sys
import heapq

def dijkstra_k_canh(adj, s, t, k):
    n = len(adj)
    dist = [[sys.maxsize] * (k + 1) for _ in range (n)]
    dist[s][0] = 0
    pq = [(0, s, 0)]

    while pq:
        d, u, edges = heapq.heappop(pq)
        if d > dist[u][edges]:
            continue
        if u == t:
            return d
        if edges >= k:
            continue
        for v, weight in adj[u]:
            nd = d + weight
            if nd < dist[v][edges + 1]:
                dist[v][edges + 1] = nd
                heapq.heappush(pq, (nd, v, edges + 1))
    return -1
