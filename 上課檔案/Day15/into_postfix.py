def into_postfix(infix):
    d = {
            '+':1,
            '-':1,
            '*':2,
            '/':2
        }
    s = []
    result = ''
    for i in infix:
        if i in ['+','-','*','/']:
            if not s:
                s.append(i)
            else:
                top = s[-1]
                while (d[i] <= d[top]) and s:
                    result += s.pop()
                    if not s: break
                    top = s[-1]
                    
                s.append(i)
                
        else:
            result += i
    while s:
        result += s.pop()

    return result