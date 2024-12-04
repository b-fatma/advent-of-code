def read_file(file_name: str):
    f = open(file_name, 'r')
    input = [line for line in f.readlines()]
    return input


def word_search(input: list):
    n = len(input)
    m = len(input[0])
    total = 0
    for i in range(n):
        for j in range(m):
            if input[i][j] == 'A':
                if j - 1 >= 0 and i - 1 >= 0 and i + 1 < n and j + 1 < m:
                    # first diagonal and second diagonal
                    if ((input[i-1][j-1] == 'M' and input[i+1][j+1] == 'S') or (input[i-1][j-1] == 'S' and input[i+1][j+1] == 'M')) and ((input[i-1][j+1] == 'M' and input[i+1][j-1] == 'S') or (input[i-1][j+1] == 'S' and input[i+1][j-1] == 'M')):
                        total += 1
                        
    return total

if __name__ == '__main__':
    input = read_file('input')
    input2 = ['MMMSXXMASM', 'MSAMXMSMSA', 'AMXSXMAAMM', 'MSAMASMSMX'
            , 'XMASAMXAMM', 'XXAMMXXAMA', 'SMSMSASXSS', 'SAXAMASAAA'
            , 'MAMMMXMMMM', 'MXMXAXMASX']
    print(word_search(input))
