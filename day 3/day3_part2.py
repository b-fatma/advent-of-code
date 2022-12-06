import itertools

def common_item(rucksack1, rucksack2, rucksack3):
    return set(rucksack1) & set(rucksack2) & set(rucksack3)

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
f = open("input.txt", 'r')
reader = f.read().split('\n')
i=0
s=0
while i < len(reader) // 3:
    print(common_item(reader[3*i], reader[3*i+1], reader[3*i+2]))
    print([alphabet.find(x)+1 for x in common_item(reader[3*i], reader[3*i+1], reader[3*i+2])])
    [s := s + alphabet.find(x)+1 for x in common_item(reader[3*i], reader[3*i+1], reader[3*i+2])]
    i += 1
print(s)
f.close()
