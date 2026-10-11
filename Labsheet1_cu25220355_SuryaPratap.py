#Stack
n=int(input("Enter the number of elements in the list: "))
a=[]
for i in range(n):
    element=int(input("Enter element: "))
    a.append(element)
while len(a)>0:
    print("The list is: ",a)
    print("the top element is: ", a[-1])
    print("The popped Element is :", a.pop())

#Queue
n=int(input("Enter the number of elements in the list: "))
my_list=[]
for i in range(n):
    element=int(input("Enter element: "))
    my_list.append(element)
while len(my_list)>0:
    print("The list is: ",my_list)
    print("the top element is: ", my_list[-1])
    print("The popped Element is :", my_list.pop(0))
