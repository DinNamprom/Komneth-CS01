lo = int(input("Enter loop: "))
score_list = []
a = 0
for i in range(lo):
    data = int(input("input score: "))
    score_list += [data]
while a <= lo -1:
    if score_list[a] < 0:
        break
    print(score_list[a])
    a += 1