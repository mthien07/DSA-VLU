import sys
import heapq

def dijkstra_dinh(n, canh, cost, s):
    adj = [[] for _ in range (n)]
    for u, v in canh:
        adj[u].append((v, cost[v]))

    dist = [sys.maxsize] * n
    dist[s] = cost[s]
    pq = [(cost[s], s)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, weight in adj[u]:
            nd = dist[u] + weight
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
