n = int(input())
for i in range(2, n+1):
    if n % i != 0: continue
    p = 0
    while n % i == 0:
        n //= i
        p += 1
    if n == 1:
        if p > 1:
            print(f'{i}^{p}')
        else:
            print(f'{i}')
    else:
        if p > 1:
            print(f'{i}^{p} *', end=' ')
        else:
            print(f'{i} *',end=' ')