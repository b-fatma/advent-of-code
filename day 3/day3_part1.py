def common_item(compartment1, compartment2):
    return set(compartment1) & set(compartment2)

def compartments(rucksack):
    return (rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:])

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
f = open("input.txt", 'r')
reader = f.readlines()
s = 0
for rucksack in reader:
    compartment1, compartment2 = compartments(rucksack)
    [s := s + alphabet.find(x)+1 for x  in common_item(compartment1, compartment2)]
print(s)
f.close()
