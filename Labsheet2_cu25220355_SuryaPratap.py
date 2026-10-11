#Binary Search 
Arr = list(map(int, input("Enter the elements : ").split()))
key = int(input("Enter the element to search: "))   
arr = sorted(Arr)  
low = 0
high = len(arr) - 1

while low<=high:
    mid = (low + high) // 2
    if arr[mid] == key:
        print("Element found at index:", mid)
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found")
 
#Linear Search 
def linear_search(arr, key):
    n = len(arr)

    for i in range(n):
        if arr[i] == key:
            return i

    return -1
arr = list(map(int, input("Enter the elements: ").split()))
key = int(input("Enter the element to search: "))
result = linear_search(arr, key)
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
