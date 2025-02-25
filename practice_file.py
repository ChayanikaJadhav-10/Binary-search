def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1
    
data = [1,22,41,3,5]
target = 3 
# print(linear_search(data,target))


def binary_search(data,target):
    low = 0
    high = len(data) - 1
    mid = low+high // 2
    
    while low<=high:
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid - 1
        else:
            high = mid+1 
            
    return -1
            
binary_search(data, target)