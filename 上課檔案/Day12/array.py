#Traversal 遍歷
a = [1,2,3,'','']#O(1)*n = O(n)
def Traversal(a):
    for i in range(len(a)): #O(1) * n = O(n)
        print(a[i]) #陣列取值 O(1)

#Total = O(n) + O(n) = O(n)

#Maximum
def Maximum(a):
    maximum = 0 #O(1)
    for i in range(1, len(a)):#O(1)*(n-1) = O(n)
        if a[i] > maximum:#O(1)
            maximum = i #O(1)
    return i #O(1)
    # O(1)+O(n)+O(1) = O(n)
# print(Maximum(a))#O(1)

#Total = O(n)

#Sum
def Sum(a):
    s = 0 #O(1)
    for i in range(len(a)):#O(1)*n = O(n)
        s += a[i] #O(1)
    return s #O(1)
    
# print(Sum(a)) #O(1)
#Total = O(1) + O(n) + O(1) + O(1) = O(n)

#Append
def Append(a, item):
    if a[-1]:#O(1)
        print('Full')#O(1)
        return a#O(1)
    for i in range(len(a)): #O(1)*3*n = O(n)
        if not(a[i]): #O(1)
            a[i] = item #O(1)
            break #O(1)
    print('Full')#O(1)
    return a#O(1)
a = Append(a, 4)#O(1)
print(a)#O(1)

#Total = O(1)*3 + O(n) + O(1)*2 + O(1) + O(1) = O(n)