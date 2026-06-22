import heapq

def dijkstra_xac_suat(adj, s, t):
    n = len(adj)
    prob = [0.0] * n
    prob[s] = 1.0
    pq = [(-1.0, s)]

    while pq:
        neg_p, u = heapq.heappop(pq)
        p = -neg_p
        if p < prob[u]:
            continue
        if u == t:
            return prob[t]
        for v, weight in adj[u]:
            np_ = p * weight
            if np_ > prob[v]:
                prob[v] = np_
                heapq.heappush(pq, (-np_, v))
    return prob[t]
