r = 0
#重複做兩次
for _ in range(2):
    #處理一場的方法
    #(1)拿主、客分數 -> 加總
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a = sum(a)
    b = sum(b)
    #(2)比較輸贏、顯示比分、記錄
    if a > b: r += 1
    else: r -= 1
    print(f'{a}:{b}')

if r > 0: print('Win')
elif r == 0: print('Tie')
else: print('Lose')