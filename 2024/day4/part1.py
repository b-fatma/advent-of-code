def read_file(file_name: str):
    f = open(file_name, 'r')
    input = [line for line in f.readlines()]
    return input


# input[i][j] == 'X'
def check_horizontally(input: list, i: int, j: int):
    m = len(input[0])

    total = 0

    # left to right
    if j + 3 < m:
        if input[i][j+1] == 'M' and input[i][j+2] == 'A' and input[i][j+3] == 'S':
            total += 1
    
    # right to left
    if j - 3 >= 0:
        if input[i][j-1] == 'M' and input[i][j-2] == 'A' and input[i][j-3] == 'S':
            total += 1
    
    return total


def check_vertically(input: list, i: int, j: int):
    n = len(input)

    total = 0

    # left to right
    if i + 3 < n:
        if input[i+1][j] == 'M' and input[i+2][j] == 'A' and input[i+3][j] == 'S':
            total += 1
    
    # right to left
    if i - 3 >= 0:
        if input[i-1][j] == 'M' and input[i-2][j] == 'A' and input[i-3][j] == 'S':
            total += 1
    
    return total

def check_diagonally(input: list, i: int, j: int):
    n = len(input)
    m = len(input[0])

    total = 0
    
    # right of input[i][j]
    if j + 3 < m:
        if i - 3 >= 0:
            if input[i-1][j+1] == 'M' and input[i-2][j+2] == 'A' and input[i-3][j+3] == 'S':
                total += 1
        if i + 3 < n:
            if input[i+1][j+1] == 'M' and input[i+2][j+2] == 'A' and input[i+3][j+3] == 'S':
                total += 1

    # left of input[i][j]
    if j - 3 >= 0:
        if i - 3 >= 0:
            if input[i-1][j-1] == 'M' and input[i-2][j-2] == 'A' and input[i-3][j-3] == 'S':
                total += 1
        if i + 3 < n:
            if input[i+1][j-1] == 'M' and input[i+2][j-2] == 'A' and input[i+3][j-3] == 'S':
                total += 1
    return total


def word_search(input: list):
    n = len(input)
    m = len(input[0])
    total = 0
    for i in range(n):
        for j in range(m):
            if input[i][j] == 'X':
                total += check_horizontally(input, i, j) + check_vertically(input, i, j) + check_diagonally(input, i, j)
    return total

if __name__ == '__main__':
    input = read_file('input')
    input2 = ['MMMSXXMASM', 'MSAMXMSMSA', 'AMXSXMAAMM', 'MSAMASMSMX'
            , 'XMASAMXAMM', 'XXAMMXXAMA', 'SMSMSASXSS', 'SAXAMASAAA'
            , 'MAMMMXMMMM', 'MXMXAXMASX']
    print(word_search(input))
