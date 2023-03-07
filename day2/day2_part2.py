shapes = {"A":1, "B":2, "C":3}
m = {"X":2, "Y":0, "Z":1}
scores = [3, 6, 0]

def round(move1, move2):
    return scores[m[move2]] + (shapes[move1] + m[move2] if shapes[move1] + m[move2] <= 3 else (shapes[move1] + m[move2]) % 3)

f = open("input.txt", 'r')
reader = f.readlines()
score = 0
for line in reader:
    player1, player2 = line.split()
    score += round(player1, player2)
print(score)
f.close()