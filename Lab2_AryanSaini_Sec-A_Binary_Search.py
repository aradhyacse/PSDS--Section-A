def binary_search(arr, target):
    n = len(arr)
    low = 0;
    high = n -1;

    while low <= high:
        mid = low + (high - low) // 2  
        
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = eval(input("Enter array: "))
target = int(input("Enter target element: "))
print(binary_search(arr, target))
