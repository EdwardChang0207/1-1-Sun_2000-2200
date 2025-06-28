#operator 運算子, operatee 運算元

#數學運算子 num op num -> num
'''
+, -, *, /(float)
**(指數) eg.2**3, a**b
%(餘數)
//(商數)
'''
# print(10//3)
# print(2**10)
# print(10/2)
#邏輯運算子
#(1) num op num -> bool
# >, <, >=, <=, !=(not equal), ==(equal) [= -> 定義(define) assign]
# print(4<5)
#(2) bool op bool -> bool
'''
邏輯閘 Logic gates
1.反閘 not gate
周杰倫：哎呦不錯喔
不(not)錯(False) -> True
錯 -> False
不(not)行(True) -> False
行 -> True

2.或閘 or gate
English or Math -> 3000
T          F       T
F          T       T
T          T       T
F          F       F
a, b = False, False
print(a or b)

3.且閘 and gate
作業 and 收座位 -> :)
T       F        F
F       T        F
T       T        T
F       F        F
a, b = False, False
print(a and b)

4.斥或閘 xor -> excursive or
珍奶 xor 烏龍拿鐵 -> :)
T       F          T
F       T          T
T       T          F
F       F          F
'''
# (1) and, or, not -> xor
a, b = False, False
print((a or b) and (not(a and b)))

# (2) ^(binary)
print(a^b)

'''
>= -> > or ==
'''

x = 1
# x(new) = x(old) + 1
# x += 1(python) x++(C)
x = x+1

print(x)