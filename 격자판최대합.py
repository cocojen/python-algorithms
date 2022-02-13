# n = int(input())

# bingo = []

# for _ in range(n):
#     row = input().split()
#     bingo.append(row)
    

# max = 0

# for i in range(n):
#     row_sum = 0 
#     col_sum = 0
#     dia_sum = 0
#     for j in range(n):
#        row_sum += bingo[i][j] 
#        col_sum += bingo[j][i]
#        dia_sum += bingo[i][i]
#     if row_sum > max:
#         max = row_sum
#     if col_sum > max:
#         max = col_sum


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

largest = 0

for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1+=a[i][j]
        sum2+=a[j][i]
    if sum1 > largest:
        largest=sum1
    if sum2 > largest:
        largest=sum2
    
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]

if sum1>largest:
    largest=sum1
if sum2>largest:
    largest=sum2

print(largest)