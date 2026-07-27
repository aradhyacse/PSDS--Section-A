arr = []

print("Enter 5 elements:")
for i in range(5):
    num = int(input(f"Element {i+1}: "))
    arr.append(num)

while(len(arr) > 0):
    arr = arr[:-1]
    print(arr)
    
print("List cleared successfully.")

