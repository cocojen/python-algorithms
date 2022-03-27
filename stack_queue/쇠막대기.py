polls = input()

stack = []

prev = ''
cnt = 0

for i in range(len(polls)):
    if polls[i] == '(':
        stack.append(polls[i])
    else:
        stack.pop()
        if polls[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1
        
print(cnt)


# (()()) - 3