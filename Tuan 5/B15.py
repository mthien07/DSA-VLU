import sys
import heapq

def dijkstra_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    dist = [[sys.maxsize] * cols for _ in range (rows)]
    dist[0][0] = grid[0][0]
    pq = [(grid[0][0], 0, 0)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while pq:
        d, x, y = heapq.heappop(pq)
        if d > dist[x][y]:
            continue
        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < rows and 0 <= ny < cols:
                nd = d + grid[nx][ny]
                if nd < dist[nx][ny]:
                    dist[nx][ny] = nd
                    heapq.heappush(pq, (nd, nx, ny))

    return dist[rows-1][cols-1]
