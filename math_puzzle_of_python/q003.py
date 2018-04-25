card = {}
for num in range(1, 101):
    card[num] = True

for n in range(2, 101):
    for m in range(n, 101, n):
        if card[m]:
            card[m] = False
        else:
            card[m] = True

answer = []
for k, v in card.items():
    if v:
        answer.append(k)

print(answer)