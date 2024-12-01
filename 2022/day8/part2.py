def view_vertically(matrix, n, i, j):
    count = 0
    for k in range(i-1, -1, -1):
        if matrix[k][j] < matrix[i][j]:
            count += 1
        else:
            if matrix[k][j] == matrix[i][j]:
                count += 1
            break
    count2 = 0    
    for k in range(i+1, n):
        if matrix[k][j] < matrix[i][j]:
            count2 += 1
        else:
            if matrix[k][j] == matrix[i][j]:
                count2 += 1
            break
    return count*count2

def view_horizontally(matrix, m, i, j):
    count = 0
    for k in range(j-1, -1, -1):
        if matrix[i][k] < matrix[i][j]:
            count += 1
        else:
            if matrix[i][k] == matrix[i][j]:
                count += 1
            break
    count2 = 0    
    for k in range(j+1, m):
        if matrix[i][k] < matrix[i][j]:
            count2 += 1
        else:
            if matrix[i][k] == matrix[i][j]:
                count2 += 1
            break
    return count*count2

def view_score(matrix, i, j, n, m):
    return view_horizontally(matrix, m, i, j) * view_vertically(matrix, n, i, j)


def parse(text):
    return text.splitlines()


if __name__ == '__main__':
    f = open("input.txt", 'r')
    matrix = parse(f.read())
    n = len(matrix)
    m = len(matrix[0])

    print(max([view_score(matrix, i, j, n, m) for i in range(n) for j in range(m)]))