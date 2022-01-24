# 5
# level
# moon
# abcba
# soon
# gooG

# 첨에 문제 제대로 안 읽어서 대소문자 구분 안한다는 거 놓침.
# 대 소문자 놓쳐서 틀리면 아깝잖어 놓치지마~~

n = int(input())

for i in range(n):
    chars = list(input().upper())
    reversed = chars[::-1]
    is_pallindrome = True
    while chars:
        if chars.pop() is not reversed.pop():
            is_pallindrome = False
            break
        
    if is_pallindrome:
        print(f'#{i+1} YES')
    else:
        print(f'#{i+1} NO')
    


# ---------------

n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)
    for j in range(size//2):
        if s[j] is not s[-1-j]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))