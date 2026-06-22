import sys
import heapq

def dijkstra_ngan_nhi(adj, s, t):
    n = len(adj)
    dist1 = [sys.maxsize] * n
    dist2 = [sys.maxsize] * n
    dist1[s] = 0
    pq = [(0, s)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist2[u]:
            continue
        for v, weight in adj[u]:
            nd = d + weight
            if nd < dist1[v]:
                dist2[v] = dist1[v]
                dist1[v] = nd
                heapq.heappush(pq, (nd, v))
            elif nd > dist1[v] and nd < dist2[v]:
                dist2[v] = nd
                heapq.heappush(pq, (nd, v))

    return dist1[t], dist2[t]
