import random
scores = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

ROWS = 3
COLS = 4

for r in range(0,ROWS):
    for c in range(0, COLS):
        scores[r][c] = random.randint(1,100)

print(scores)
