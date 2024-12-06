from part1 import read_file, move

# directions : [0: up, 1: right, 2: down, 3: left]
DIRECTION_VECTORS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def check_for_loop(map, initial_direction, initial_pos, n, m):
    seen = set()
    terminated = False
    i, j = initial_pos
    direction = initial_direction

    while not terminated:
        di, dj = DIRECTION_VECTORS[direction] 
        ni, nj = i + di, j + dj
        
        if not (0 <= ni < n and 0 <= nj < m):
            terminated = True 
            break
        elif map[ni][nj] == '#':
            direction = (direction + 1) % 4  
        else:
            i, j = ni, nj
        
        if (i, j, direction) in seen:
            return True  # Loop detected
        seen.add((i, j, direction))

    return False


def brute_force(map, visited, pos, direction, n, m):
    sum = 0
    for location in visited:
        i, j = location
        map[i][j] = '#'
        if check_for_loop(map, direction, pos, n, m):
            sum += 1
        map[i][j] = '.'
    return sum



if __name__ == '__main__':
    direction, pos, map = read_file("input")

    # map = [
    #         ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
    #         ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
    #         ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    #         ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
    #         ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
    #         ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    #         ['.', '#', '.', '.', '^', '.', '.', '.', '.', '.'],
    #         ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
    #         ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    #         ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.']
    # ]
    # pos = (6, 4)
    
    n = len(map)
    m = len(map[0])

    visited = move(map, direction, pos, n, m)
    print(brute_force(map, visited, pos, direction, n, m))
