def is_safe(input: list[int]):
    ascending = input[0] < input[1]

    for i  in range(len(input) - 1):
        diff = input[i+1] - input[i]

        if (ascending and diff <= 0) or (not ascending and diff>0):
            return 0
        
        if abs(diff) > 3 or abs(diff) < 1:
            return 0    
    return 1
    

def process_file(filename: str):
    f = open(filename, 'r')
    sum = 0
    for line in f.readlines():
        sum += is_safe(list(map(int, line.split())))
    return sum

print(process_file('input'))


