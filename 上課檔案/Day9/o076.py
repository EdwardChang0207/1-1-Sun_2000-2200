n = int(input())
h = list(map(int, input().split()))
max_path, cur_path = 0, 1

last_h = h[0]
for i in range(1, len(h)):
    if h[i]<last_h:
        cur_path += 1
        
    else:
        max_path = max(max_path, cur_path)
        cur_path = 1
    last_h = h[i]
max_path = max(max_path, cur_path)
print(max_path)