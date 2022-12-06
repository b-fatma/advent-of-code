def uniqueChar(string):
    return len(set(string)) == len(string)

def search(f, length):
    string = f.read(length)
    while len(set(string)) != length:
        string = string[1:] + f.read(1)
    return f.tell()

if __name__ == '__main__':
    f = open('input.txt', 'r')
    print("part 1: ", search(f, 4), "\npart 2: ", search(f, 14))
    f.close()
