def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    
    return -1


arr = eval(input("Enter array: "))
target = int(input("Enter target element: "))
print(linear_search(arr, target))
