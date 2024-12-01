def read_input(file_name):
    f = open(file_name, 'r')
    i = 0
    locations_a = list()
    locations_b = list()
    for line in f.readlines():
        a, b = line.split()
        locations_a.append(int(a))
        locations_b.append(int(b))
    return locations_a, locations_b

def frequency(lista: list):
    frequency_map = {}
    for num in lista:
        frequency_map[num] = frequency_map.get(num, 0) + 1
    return frequency_map

def compute_result(lista: list, listb: list):
    frequency_map = frequency(listb)
    sum = 0
    for x in lista:
        sum += x * frequency_map.get(x, 0)
    return sum

list1 , list2 = read_input('input')
dist = compute_result(list1, list2)
print(dist)
