a = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]
a.pop(0)
for x in a:
    print(x, end=' ')


# 5 10
# 9 13
# 1 2
# 3 4 
# 5 6 
# 1 2 
# 3 4 
# 5 6 
# 1 20 
# 1 20

# 1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20