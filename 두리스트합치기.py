n = int(input())
list_a = list(map(int, input().split()))

m = int(input())
list_b = list(map(int, input().split()))


list_c = (list_a + list_b)
print(list_c)
list_c.sort()

for x in list_c:
    print(x, end=' ')

# 3
# 1 3 5
# 5
# 2 3 6 7 9

# n = int(input())
# a = list(map(int, input().split()))

# m = int(input())
# b = list(map(int, input().split()))

# p1=p2=0
# c = []
# while p1<n and p2<m:
#     if a[p1] <= b[p2]:
#         c.append(a[p1])
#         p1+=1
#     else:
#         c.append(b[p2])
#         p2+=1
        
# if p1<n:
#     c=c+a[p1:]
# if p2<m:
#     c=c+b[p2:]
    

# for x in c:
#     print(x, end= ' ')