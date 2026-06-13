N = int(input())
ruiseki = [[0]*1501 for _ in range(1501)]
for _ in range(N):
    a, b, c, d = map(int, input().split())
    ruiseki[a][b] += 1
    ruiseki[c][d] += 1
    ruiseki[a][d] -= 1
    ruiseki[c][b] -= 1

for i in range(1501):
    total = 0
    for j in range(1501):
        total += ruiseki[i][j]
        ruiseki[i][j] = total

for j in range(1501):
    total = 0
    for i in range(1501):
        total += ruiseki[i][j]
        ruiseki[i][j] = total

ans = 0

for i in range(1501):
    for j in range(1501):
        if ruiseki[i][j] >= 1:
            ans += 1

print(ans)