def contains(a, b):
    return ((a[0] <= b[0]) and (a[-1] >= b [-1]))

def overlaps(a, b):
    return a[0] >= b[0] and a[0] <= b[1] or a[1] <= b[1] and a[1] >= b[0]

contained = 0
overlapping = 0
f = open("input.txt", 'r')
reader = f.readlines()
for line in reader:
    range1, range2 =  [list(map(int,x.split('-'))) for x in line.strip('\n').split(',')]
    if contains(range1, range2) or contains(range2, range1):
        contained += 1
    if overlaps(range1, range2) or overlaps(range2, range1):
        overlapping += 1
print(contained, overlapping)
f.close()