Queue=[]
# adding done at end
# remove done at front

def enqueue():
    item=int(input("Enter the Elememt : "))
    Queue.append(item)
    print("Item Enqueued ",Queue)
def dequeue():
    if not Queue:
        print("Queue Empty ")
    else:    
        e=Queue.pop(0)    
        print("removed item ",e)
        
def display():
    print("Queue : ",Queue)      
    
while True:
    print("SElect a valid operation to perform . \n1 add ,\n2 remove ,\n3Display,\n4 Quit") 
    choice =int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Invalid Choice ")        
        