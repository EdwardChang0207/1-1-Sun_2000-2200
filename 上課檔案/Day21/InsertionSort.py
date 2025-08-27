def swap(a, b):
    return b, a

def Insert(i, data):
    for j in range(i, -1, -1):
        if data[j] > data[j-1]:
            return data
        if data[j] < data[j-1]:
            data[j], data[j-1] = swap(data[j], data[j-1])
    return data
        
def InsertionSort(data): #O(n^2)
    n = len(data)
    for i in range(1, n+1): #1~n-1
        data = Insert(i-1, data)#0~n-2
    return data

l = [5,4,3,2,1]
print(InsertionSort(l))