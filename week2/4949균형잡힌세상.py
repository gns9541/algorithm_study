while True:
    word = input()
    if word == '.':
        break
    stack = []
    ans = 1
    for i in word:
        if i == '(':
            stack.append(i)
        elif i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                ans = 0
                break
            elif stack[-1] == '(':
                stack.pop()
            elif stack[-1] == '[':
                ans = 0
                break     
        elif i == ']':
            if len(stack) == 0:
                ans = 0
                break
            elif stack[-1] == '[':
                stack.pop()
            elif stack[-1] == '(':
                ans = 0
                break
            
    if ans == 1 and len(stack) == 0:
        print('yes')
    else:
        print('no')
