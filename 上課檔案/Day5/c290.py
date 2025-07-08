n = input()
a = n[0::2]
b = n[1::2]
A = sum(list(map(int, a)))
B = sum(list(map(int, b)))
print(abs(A-B))