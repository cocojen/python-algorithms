from audioop import reverse


N, K = map(int, input().split())

a = list(map(int, input().split()))
res = set()

for i in range(N):
    for j in range(i+1, N):
        for m in range(j+1, N):
            res.add(a[i] + a[j] + a[m])

res = list(res)
res.sort(reverse=True)
print(res[K-1])

# 10 3
# 13 15 34 23 45 65 33 11 26 42