stack = []
def push():
    item= int(input("Enter elemet"))
    stack.append(item)
    print (stack)
    
def pop():
    if len(stack)==0:
        print("Stack is empty")
    else:
        item=stack.pop()
        print ("Popped item is",item)
        print (stack)
        
while True:
    print("\n1. Push\n2. Pop\n3. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("Invalid choice")
    


