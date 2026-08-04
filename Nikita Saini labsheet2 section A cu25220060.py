# Linear Search implementation  in Python

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i 
    return -1
numbers = [10, 25, 30, 45, 50]
key = int(input("Enter the number to search: "))
result = linear_search(numbers, key)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")



# Binary Search implementation in Python    
arr = [10, 20, 30, 40, 50]
key = int(input("Enter element to search: "))
low = 0
high = len(arr) - 1
while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print("Element found at index", mid)
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found")