# kdk1k0kdjfkj0kkdjkfj0fkd

# 1000
# 16


s = list(input())

num = ''

for i in range(len(s)):
    if s[i].isdigit():
        num = num + s[i]

num = int(num)

print(f'# {num}')

cnt = 0
for i in range(1, num+1):
    if num % i == 0:
        cnt += 1

print(f'# {cnt}')