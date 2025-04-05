```python
from collections import deque

def shortest_path(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(0,1), (1,0), (0,-1), (-1,0)]  # Right, Down, Left, Up

    # Find the start (0,0) and exit ('E')
    start = (0, 0)
    exit_pos = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'E':
                exit_pos = (r, c)

    if not exit_pos:
        return -1  # No exit found

    # BFS Setup
    queue = deque([(start[0], start[1], 0)])  # (row, col, steps)
    visited = set()
    visited.add(start)

    # BFS Traversal
    while queue:
        r, c, steps = queue.popleft()

        # If we reached the exit
        if (r, c) == exit_pos:
            return steps

        # Explore neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                if grid[nr][nc] != 1:  # Not a sentinel (1 is blocked)
                    queue.append((nr, nc, steps + 1))
                    visited.add((nr, nc))

    return -1  # If no path found

# Read input as a string, then evaluate it to convert into a proper Python list
input_text = input()  # e.g., "[[0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], ...]"

# Use eval to convert the string into an actual list (be cautious with eval in real-world applications)
grid = eval(input_text)

# Run the algorithm to find the shortest path
result = shortest_path(grid)
print(result)

```

`HTB{CL0CKW0RK_GU4RD14N_OF_SKYW4TCH_41bc88d0369291209262fbc2db46d267}`