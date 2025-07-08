n, d = map(int,input().split())
amount, price = 0, 0
for _ in range(n):
    #商品價格
    p = list(map(int, input().split()))
    #檢查一個商品的價格
    if max(p)-min(p) >= d:
    #如果要購買 -> 計算平均 -> 記錄
        price += sum(p)//len(p)
        amount += 1

print(amount, price)