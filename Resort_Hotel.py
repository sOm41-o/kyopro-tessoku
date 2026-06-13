N = int(input())
A = list(map(int, input().split()))
P = [0]*(N + 1)
Q = [0]*(N + 1)
P[0] = A[0]
D = int(input())
for i in range(1, N):
    P[i] = max(P[i - 1], A[i])
for i in range(N - 1, -1, -1):
    Q[i] = max(Q[i + 1], A[i])
print(P)
print(Q)
for i in range(D):
    l, r = map(int, input().split())
    print(max(P[l - 2], Q[r]))