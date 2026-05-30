N, M = map(int, input().split())
masu = [1]*(N + 1)
for _ in range(M):
    l, r = map(int, input().split())
    masu[l] += 1
    masu[r] -= 1