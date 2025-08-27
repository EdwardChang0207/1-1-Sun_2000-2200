def swap(a, b):
    return b, a

def BubbleSort(data):#O(n^2)
    n = len(data)
    for i in range(n-1):#R
        for j in range(n-i-1): #step
            if data[j+1] < data[j]:
                data[j+1], data[j] = swap(data[j+1], data[j])
    return data

l = [5,4,3,2,1]
print(BubbleSort(l))