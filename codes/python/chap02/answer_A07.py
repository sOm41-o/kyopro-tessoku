D = int(input())
N = int(input())

attendances = [0]*(D + 1)  # 0埋めしておくこと。

for _ in range(N):
    l, r = map(int, input().split())
    attendances[l - 1] += 1
    attendances[r] -= 1

total = 0
for i in range(D):
    total += attendances[i]
    print(total)