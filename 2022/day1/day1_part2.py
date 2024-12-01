f = open("input.txt", 'r')
reader = f.readlines()
sumList = []
cal = 0
for line in reader:
    if line == '\n':
        sumList.append(cal)
        cal = 0
    else:
        cal += int(line)
print(sum(sorted(sumList)[-3:]))