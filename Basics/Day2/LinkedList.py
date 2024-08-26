# Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.ref= None

class LinkedList:
    def __init__(self):
        self.head = None    
    # TRAVERSAL IN LINKED LIST
    def print_ll(self):
        if self.head is None:
            print("Linked List is empty")
            return
        else:
            n=self.head
            while n is not None:
                print(n.data,"--->",end=" ")
                # print(n.ref,"--->",end=" ")
                n=n.ref
     
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node   
    
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref=new_node            
                
    def add_between(self,data1,data2): 
        n=self.head
        while n  is not None:
            if data2==n.data1:
                break
            n=n.ref
                 
                
LL1 =LinkedList()   
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
LL1.print_ll()  
LL1.add_end(50)     
LL1.print_ll()       