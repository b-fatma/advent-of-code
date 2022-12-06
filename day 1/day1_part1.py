f = open("input.txt", 'r')
maxCalories = 0
calories = 0
fr = f.readlines()
for line in fr:
    if line == '\n':
        if calories > maxCalories:
            maxCalories = calories
        calories = 0
    else:
        calories += int(line)
print(maxCalories)