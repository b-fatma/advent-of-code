def read_file(filename):
    f = open(filename, 'r')
    data = f.read()
    rulings, orders = data.split('\n\n')
    
    # building successors dictionary
    successors = dict()
    for ruling in rulings.split('\n'):
        x, y = map(int, ruling.split("|"))
        if x not in successors.keys():
            successors[x] = []
        successors[x].append(y)
    
    # building page orders
    orders = [list(map(int, order.split(","))) for order in orders.split()]
    return successors, orders

def valid_order(successors, order):
    n = len(order)
    correct = True
    for i in range(n - 1):
        key = order[i]
        for j in range(i+1, n):
            if order[j] not in successors.get(order[i], []):
                correct = False
                break
        if not correct:
            break
    return correct

def bubble_sort(successors, order):
    n = len(order)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            # If `order[i]` should be after `order[i+1]`
            if order[i] in successors.get(order[i + 1], []):
                # Swap adjacent elements
                order[i], order[i + 1] = order[i + 1], order[i]
                swapped = True
    return order

def compute_sum(successors, orders):
    sum = 0
    for order in orders:
        if not valid_order(successors, order):
            order = bubble_sort(successors, order)
            sum += order[len(order) // 2]
    return sum


if __name__ == "__main__":
    successors, orders = read_file("input")
    print(compute_sum(successors, orders))