players_and_kscore = input().split(" ")
scores = input().split(" ")
next_round_participants = 0
lowest_score = int(scores[0])
for index, i in enumerate(scores):
    if index > 1:
        if i < scores[index - 1]:
            lowest_score = i

    if int(i) > int(players_and_kscore[1]):
        next_round_participants += 1
    else:
        if lowest_score == int(players_and_kscore[1]):
            next_round_participants += 1
print(next_round_participants)

# I understand the problem wrong
