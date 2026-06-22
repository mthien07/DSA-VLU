import heapq

def k_shortest(adj, s, t, K):
    n = len(adj)
    count = [0] * n
    pq = [(0, s)]
    result = []

    while pq and count[t] < K:
        d, u = heapq.heappop(pq)
        count[u] += 1
        if u == t:
            result.append(d)
            if len(result) == K:
                break
        if count[u] <= K:
            for v, weight in adj[u]:
                heapq.heappush(pq, (d + weight, v))
    return result
