import sys
import heapq

def dijkstra_fuel(adj, s, t, max_fuel, fuel_cost):
    n = len(adj)
    dist = [[sys.maxsize] * (max_fuel + 1) for _ in range (n)]
    dist[s][0] = 0
    pq = [(0, s, 0)]

    while pq:
        cost, u, fuel = heapq.heappop(pq)
        if cost > dist[u][fuel]:
            continue
        if u == t:
            return cost
        if fuel_cost[u] >= 0 and fuel < max_fuel:
            nc = cost + fuel_cost[u]
            if nc < dist[u][fuel + 1]:
                dist[u][fuel + 1] = nc
                heapq.heappush(pq, (nc, u, fuel + 1))
        for v, weight in adj[u]:
            if fuel >= weight and cost < dist[v][fuel - weight]:
                dist[v][fuel - weight] = cost
                heapq.heappush(pq, (cost, v, fuel - weight))
    return -1
