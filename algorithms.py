import heapq

def dijkstra(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    pq = [(0, start)]  # (cost, node)
    parent = {start: None}

    while pq:
        cost, current = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)

        if current == end:
            return reconstruct_path(parent, end)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                if neighbor not in visited:
                    heapq.heappush(pq, (cost + 1, neighbor))
                    parent[neighbor] = current

    return []  # No path found

def a_star(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    open_set = [(0, start)]
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}
    parent = {start: None}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == end:
            return reconstruct_path(parent, end)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g_score = g_score.get(current, float('inf')) + 1
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    parent[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return []  # No path found

def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])  # Manhattan Distance

def reconstruct_path(parent, end):
    path = []
    while end:
        path.append(end)
        end = parent.get(end)
    return path[::-1]
