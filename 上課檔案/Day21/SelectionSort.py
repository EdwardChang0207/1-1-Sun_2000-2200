def swap(a, b):
    return b, a

def SelectionSort(data):
    n = len(data)
    for i in range(n-1):
        key = i
        for j in range(i, n):
            if data[j] < data[key]:
                key = j
        data[i], data[key] = swap(data[i], data[key])
    return data

l = [5,4,3,2,1]
print(SelectionSort(l))