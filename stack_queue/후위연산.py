chars = input()


num_stack = []
math_stack = []

for char in chars:
    if char.isdecimal():
        num_stack.append(int(char))
    else:
        latter = num_stack.pop()
        former = num_stack.pop()
        
        if char == '+':
            ans = former + latter
        if char == '-':
            ans = former - latter
        if char == '*':
            ans = former * latter
        if char == '/':
            ans = former / latter
            
        num_stack.append(ans)
    
print(num_stack.pop())


# 352+*9-