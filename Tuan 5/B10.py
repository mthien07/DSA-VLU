import sys
import heapq
import time
import random

def dijkstra_mang(adj, s):
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

def dijkstra_heap(adj, s):
    n = len(adj)
    dist = [sys.maxsize] * n
    dist[s] = 0
    pq = [(0, s)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, weight in adj[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    return dist

def tao_do_thi(n, m):
    adj = [[] for _ in range (n)]
    for _ in range (m):
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v:
            adj[u].append((v, random.randint(1, 100)))
    return adj

def so_sanh_hieu_nang(n, m):
    adj = tao_do_thi(n, m)
    
    t1 = time.time()
    dijkstra_mang(adj, 0)
    t2 = time.time()
    time_mang = t2 - t1

    t1 = time.time()
    dijkstra_heap(adj, 0)
    t2 = time.time()
    time_heap = t2 - t1

    print(f"O(V^2): {time_mang:.4f}s")
    print(f"Heap: {time_heap:.4f}s")
