arr=[]
for i in range(5):
    a=int(input("Enter element: "))
    arr.append(a)
while len(arr)>0:
    arr=arr[:-1]
    print(arr)

