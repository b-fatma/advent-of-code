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

def compute_cumulative_distance(lista, listb):
    sum = 0
    assert(len(lista) == len(listb))
    for i in range(len(lista)):
        sum += abs(lista[i] - listb[i])
    return sum


list1 , list2 = read_input('input')
dist = compute_cumulative_distance(sorted(list1), sorted(list2))
print(dist)
        
