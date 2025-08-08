from into_postfix import into_postfix
def plus(x,y):
    return x+y
def minus(x,y):
    return x-y
def mult(x,y):
    return x*y
def divide(x,y):
    return x/y

infix = input()
postfix = into_postfix(infix)
s = []

for i in postfix:
    if i in ['+','-','*','/']:
        y, x = s.pop(), s.pop()
        if i == '+': s.append(plus(x,y))
        elif i == '-': s.append(minus(x,y))
        elif i == '*': s.append(mult(x,y))
        elif i == '/': s.append(divide(x,y))

    else:
        s.append(int(i))

print(s[-1])