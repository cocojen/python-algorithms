# 강의의 답과 똑같이 풀었음

n, k = map(int, input().split())
cnt = 0
for i in range(1, n+1):
    if n%i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)