import sys
import heapq

def dijkstra_grid(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])
    dist = [[sys.maxsize] * cols for _ in range (rows)]
    dist[start[0]][start[1]] = 0
    pq = [(0, start[0], start[1])]
    dem = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while pq:
        d, x, y = heapq.heappop(pq)
        if d > dist[x][y]:
            continue
        dem += 1
        if (x, y) == end:
            return d, dem
        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != -1:
                nd = d + 1
                if nd < dist[nx][ny]:
                    dist[nx][ny] = nd
                    heapq.heappush(pq, (nd, nx, ny))
    return -1, dem

def astar_grid(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])
    dist = [[sys.maxsize] * cols for _ in range (rows)]
    dist[start[0]][start[1]] = 0
    h = abs(start[0] - end[0]) + abs(start[1] - end[1])
    pq = [(h, 0, start[0], start[1])]
    dem = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while pq:
        f, g, x, y = heapq.heappop(pq)
        if g > dist[x][y]:
            continue
        dem += 1
        if (x, y) == end:
            return g, dem
        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != -1:
                ng = g + 1
                if ng < dist[nx][ny]:
                    dist[nx][ny] = ng
                    nh = abs(nx - end[0]) + abs(ny - end[1])
                    heapq.heappush(pq, (ng + nh, ng, nx, ny))
    return -1, dem

def bellman_grid(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])
    dist = [[sys.maxsize] * cols for _ in range (rows)]
    dist[start[0]][start[1]] = 0
    dem = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for _ in range (rows * cols - 1):
        updated = False
        for x in range (rows):
            for y in range (cols):
                if dist[x][y] == sys.maxsize:
                    continue
                dem += 1
                for i in range (4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != -1:
                        if dist[x][y] + 1 < dist[nx][ny]:
                            dist[nx][ny] = dist[x][y] + 1
                            updated = True
        if not updated:
            break
    return dist[end[0]][end[1]], dem
