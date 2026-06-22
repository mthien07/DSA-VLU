import sys
import heapq

def dijkstra_minimax(adj, s, t):
    n = len(adj)
    bottleneck = [sys.maxsize] * n
    bottleneck[s] = 0
    pq = [(0, s)]

    while pq:
        b, u = heapq.heappop(pq)
        if b > bottleneck[u]:
            continue
        if u == t:
            return bottleneck[t]
        for v, weight in adj[u]:
            nb = max(b, weight)
            if nb < bottleneck[v]:
                bottleneck[v] = nb
                heapq.heappush(pq, (nb, v))
    return bottleneck[t]
