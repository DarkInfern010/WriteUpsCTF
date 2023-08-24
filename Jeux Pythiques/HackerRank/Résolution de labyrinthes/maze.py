from collections import deque

def dfs(maze):
    for i in range(len(maze)):
        if 'D' in maze[i]:
            start = (i, maze[i].index('D'))
        if 'A' in maze[i]:
            end = (i, maze[i].index('A'))

    axes = {'G': (0, -1), 'D': (0, 1), 'H': (-1, 0), 'B': (1, 0)}

    def near(pos):
        neighbors = []
        for direction, move in axes.items():
            neighbor = (pos[0] + move[0], pos[1] + move[1])
            if neighbor[0] < 0 or neighbor[0] >= len(maze) or neighbor[1] < 0 or neighbor[1] >= len(maze[0]):
                continue
            if maze[neighbor[0]][neighbor[1]] == '#':
                continue
            neighbors.append(neighbor)
        return neighbors

    wait_list = deque()
    wait_list.append(start)
    already_path = {start: None}

    while wait_list:
        pos = wait_list.popleft()
        if pos == end:
            break
        for neighbor in near(pos):
            if neighbor not in already_path:
                already_path[neighbor] = pos
                wait_list.append(neighbor)

    if end not in already_path:
        return None
    path = []
    pos = end
    while pos is not None:
        last = already_path[pos]
        if last is not None:
            for direction, move in axes.items():
                if move == (pos[0] - last[0], pos[1] - last[1]):
                    path.append(direction)
                    break
        pos = last
    path.reverse()
    return path


maze = [input() for _ in range(21)]
path = dfs(maze)

print(path)