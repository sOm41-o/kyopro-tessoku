N, K = map(int, input().split())
Array = []
L = []

for _ in range(N):
    A = list(map(int, input().split()))
    Array.append(A[1:])
    L.append(A[0])

C = list(map(int, input().split()))
# --------------------- #
copy_K = K  # K: 値を取得したいindex保存用の変数
for i in range(N):  # ここで、オーバーする必要ない配列ははじきたい
    if copy_K <= L[i]*C[i]:
        memo = i
        break
    copy_K = copy_K - L[i]*C[i]

if copy_K == 0:
    arr = Array[memo - 1]
    print(arr[-1])

else:
    arr = Array[memo]
    print(arr[copy_K%L[memo] - 1])

# print("test")
# print(copy_K, memo)
# print(arr)