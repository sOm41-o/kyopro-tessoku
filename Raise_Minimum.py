import heapq

N, K = map(int, input().split())
A = list(map(int, input().split()))

new_A = []
for i, a in enumerate(A):
    new_A.append([a, i + 1])

heapq.heapify(new_A)

for i in range(K):
    memo = heapq.heappop(new_A)
    memo2 = heapq.heappop(new_A)  # 残りのターンで2番目に小さい値にどうやっても追いつけん→残りのターン数*iをプラス！
    if memo[0] + memo[1]*(K - i) <= memo2[0]:
        print(memo[0] + memo[1]*(K - i))
        exit()
    heapq.heappush(new_A, [memo[0] + memo[1], memo[1]])

print(heapq.heappop(new_A)[0])