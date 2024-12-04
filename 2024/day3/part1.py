import re

def read_file(file_name: str):
    f = open(file_name, 'r')
    sum = 0
    for line in  f.readlines():
        sum += evaluate_muls(process_line(line))
    return sum


def process_line(input: str):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    valid_mul = re.findall(pattern, input)
    return valid_mul

def evaluate_muls(input: list):
    sum = 0
    for a, b in input:
        sum += int(a) * int(b)
    return sum

# x = process_line("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")
# print(evaluate_muls(x))

print(read_file("input"))