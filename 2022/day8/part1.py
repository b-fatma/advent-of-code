def visible_vertically(matrix, m, i, j):
    return (all(matrix[i][k] < matrix[i][j] for k in range(j))
            or all(matrix[i][k] < matrix[i][j] for k in range(j+1, m)))

def visible_horizontally(matrix, n, i, j):
    return (all(matrix[k][j] < matrix[i][j] for k in range(i))
            or all(matrix[k][j] < matrix[i][j] for k in range(i+1, n)))

def visible(matrix, n, m, i, j):
    return visible_vertically(matrix, m, i, j) or visible_horizontally(matrix, n, i, j)

def parse(text):
    return text.splitlines()


if __name__ == '__main__':
    f = open("input.txt", 'r')
    matrix = parse(f.read())
    n = len(matrix)
    m = len(matrix[0])

    s = 0
    for i in range(n):
        for j in range(m):
            if visible(matrix, n, m, i, j):
                s += 1

    print(s)
