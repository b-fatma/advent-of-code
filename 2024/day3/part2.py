import re

def read_file(file_name: str):
    f = open(file_name, 'r')
    sum = 0
    data = f.read()
    sum += process_line(data)
    return sum


def process_line(input: str):
    do = True
    sum = 0
    partitioned_input = re.split(r"(do|don't)\(\)", input)
    for partition in partitioned_input:
        if partition == "do":
            do = True
        elif partition == "don't":
            do = False
        elif do:
            sum += process_partition(partition)
    return sum

def process_partition(input: str):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    valid_mul = re.findall(pattern, input)
    return evaluate_muls(valid_mul)

def evaluate_muls(input: list):
    sum = 0
    for a, b in input:
        sum += int(a) * int(b)
    return sum


print(read_file("input"))