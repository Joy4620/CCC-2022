N = int(input())
players = [[int(input()) for _ in range(2)] for _ in range(N)]
count = 0
for i in players:
    if (i[0]*5)-(i[1]*3) > 40:
        count += 1
        # print((i[0]*5)-(i[1]*3))

print(f'{count}+') if count == N else print(count)
