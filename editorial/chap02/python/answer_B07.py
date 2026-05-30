T = int(input())
N = int(input())

attendances = [0]*(T + 1)
for _ in range(N):
    l, r = map(int, input().split())
    attendances[l] += 1
    attendances[r] -= 1  # R + 0.5にはもういない→r + 1ではなく、just"r"で引き算！

total = 0

for i in range(T):
    total += attendances[i]
    print(total)