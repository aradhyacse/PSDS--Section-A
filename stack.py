import numpy as np
arr=np.array([1,2,3])
#push
arr=np.append(arr,4)
print("After Push:",arr)
#pop
arr=np.delete(arr,-1)
print("After pop:",arr)

#Question 2
import numpy as np 
#QUEUE
queue=np.array([],dtype=int)
#ENQ
for item in [10,20,30]:
    queue=np.append(queue,item)
    print("After ENQ",item,":",queue)
#DEQ
while len(queue)>0:
    print("Dequeued",queue[0])
    queue=np.delete(queue,0)
    print("Queue",queue)