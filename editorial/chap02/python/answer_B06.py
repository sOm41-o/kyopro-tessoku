N, Q = map(int, input().split())
A = list(map(int, input().split()))

ruiseki_A = [0]
total = 0

for a in A:
    total += a
    ruiseki_A.append(total)

for _ in range(Q):
    l, r = map(int, input().split())
    print(ruiseki_A[r] - ruiseki_A[l - 1])