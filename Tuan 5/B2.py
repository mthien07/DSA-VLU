import sys

def dijkstra_tung_buoc(adj, s):
    n = len(adj)
    dist = [sys.maxsize] * n
    dist[s] = 0
    visited = [False] * n
    thu_tu = []

    for buoc in range (n):
        min_d = sys.maxsize
        u = -1
        for i in range (n):
            if not visited[i] and dist[i] < min_d:
                min_d = dist[i]
                u = i
        if u == -1:
            break
        visited[u] = True
        thu_tu.append(u)

        for v, weight in adj[u]:
            if not visited[v] and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

        tmp = []
        for d in dist:
            if d == sys.maxsize:
                tmp.append("INF")
            else:
                tmp.append(str(d))
        print(f"Buoc {buoc + 1}: chot dinh {u}, dist = {tmp}")

    print(f"Thu tu chot: {thu_tu}")
    print(f"dist cuoi: {dist}")
