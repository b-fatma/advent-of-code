def read_file(filename: str):
    f = open(filename, 'r')
    eqs = {}
    for line in f.readlines():
        result, operands = line.split(":")
        eqs[int(result)] = list(map(int, operands.strip().split(" ")))
    return eqs

def evaluate_left_to_right(operands, i, current_value):
    if i == len(operands):
        return [current_value]  
    
    results = []
    
    results += evaluate_left_to_right(operands, i + 1, current_value + operands[i])
    results += evaluate_left_to_right(operands, i + 1, current_value * operands[i])
    # for part 2 
    # || operator
    results += evaluate_left_to_right(operands, i + 1, int(str(current_value) + str(operands[i])))

    return results

def get_total_calibration_result(equations):
    sum = 0
    for result in equations:
        if any([result in evaluate_left_to_right(equations[result], 1, equations[result][0])]):
            sum += result
    return sum


if __name__ == "__main__":
    equations = read_file("input")
    print(get_total_calibration_result(equations))




# useful if we needed to respect the precedence of operators
# def generate_combinations(operands, i):
#     if i == len(operands) - 1:
#         return [str(operands[i])]  
    
#     next_combinations = generate_combinations(operands, i + 1)
#     results = []
    
#     for expr in next_combinations:
#         results.append(str(operands[i]) + " + " + expr)
#         results.append(str(operands[i]) + " * " + expr)
    
#     return results