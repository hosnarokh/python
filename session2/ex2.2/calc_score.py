counter = 30
win = 0
total_score = 0
while counter > 0:
    score = int(input())
    if score == 3:
        win += 1
    total_score += score
    counter = counter - 1
print(total_score, win)
