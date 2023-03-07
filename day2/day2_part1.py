shapes = {"A":1, "X":1, "C":3, "Z":3, "B":2, "Y":2}
scores = [3, 0, 6]

def round(move1, move2):
    return shapes[move2] + scores[shapes[move1] - shapes[move2]]

f = open("input.txt", 'r')
reader = f.readlines()
score = 0
for line in reader:
    player1, player2 = line.split()
    score += round(player1, player2)

print(score)
f.close()
