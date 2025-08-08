'''
algo:
while not scan over:
    if i is 'f(' or operatee -> push
    if i is ')'
        step1. pop until u meet 'f('
        step2. collect all nums u pop from stack -> l
        step3. find maximum and minimum of the nums u just pop
        step4. cal maximum - minimum, then name the ans as 'r'
        step5. push 'r' into stack
print(s.top)
'''
def f(infix):
    s = [] 
    idx = 0
    num = ''
    while idx < len(infix):
        if infix[idx]=='f' and infix[idx+1]=='(':
            s.append(infix[idx:idx+2])
            idx += 1
        elif infix[idx] == ')':
            if num:
                s.append(num)
                num = ''
            l = []
            while s[-1] != 'f(':
                i = s.pop()
                if ('+' in i) or ('*' in i):
                    i = cal(i)
                l.append(int(i))
            s.pop()
            r = max(l)-min(l)
            s.append(r)
        elif infix[idx] == ',':
            if num:
                s.append(num)
                num = ''
        else:
            num += infix[idx]
        idx += 1
    return s[-1]
#只有＋＊
def cal(infix):
    r = 1
    for i in infix.split('*'):
        p = 0
        j = i.split('+')
        for k in j:
            p += int(k)
        r *= p
    return r
        
#stack
#all
infix = input()
idx = 0
s = []
while idx < len(infix):
    if infix[idx] == 'f':
        s.append(idx)
    idx += 1
while s:
    i = s.pop()
    j = i
    while infix[j] != ')': j += 1
    infix = infix[:i:]+str(f(infix[i:j+1]))+infix[j+1::]
print(cal(infix))

