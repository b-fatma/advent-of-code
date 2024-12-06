def read_file(filename: str):
    f = open(filename, 'r')
    directions = ["^", ">", "v", "<"]
    i = 0
    map = []
    for line in f.readlines():
        m = len(line)
        for j in range(m):
            if line[j] in directions:
                pos = (i, j)
                direction = directions.index(line[j])
        i += 1
        map.append(list(line.strip()))
    return direction, pos, map

# directions : [0: up, 1: right, 2: down, 3: left]
DIRECTION_VECTORS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def move(map, direction, pos, n, m):
    visited = set()
    i ,j = pos
    while True:
        di, dj = DIRECTION_VECTORS[direction]
        ni, nj = i + di, j + dj

        if not (0 <= ni < n and 0 <= nj < m):
            break

        if map[ni][nj] == '#':
            direction = (direction + 1) % 4
        else:
            i, j = ni, nj
            visited.add((i, j))

    return visited


# directions : [0: up, 1: right, 2: down, 3: left]
if __name__ == '__main__':
    direction, pos, map = read_file("input")

    # map = [
    # "....#.....",
    # ".........#",
    # "..........",
    # "..#.......",
    # ".......#..",
    # "..........",
    # ".#..^.....",
    # "........#.",
    # "#.........",
    # "......#..."
    # ]
    # pos = (6, 4)
    
    n = len(map)
    m = len(map[0])


    print(len(move(map, direction, pos, n, m)))

