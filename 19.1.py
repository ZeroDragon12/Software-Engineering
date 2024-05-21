def calc():
    expression = input().split()
    stack = []
    for i in expression:
        if i.isnumeric():
            stack.append(int(i))
        else:
            i1, i2 = stack.pop(), stack.pop()
            if i == '+':
                stack.append(i1 + i2)
            elif i == '-':
                stack.append(i2 - i1)
            elif i == '*':
                stack.append(i1 * i2)
            else:
                stack.append(i2 // i1)
    print(stack[0])

calc()