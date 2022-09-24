class Node:
    def __init__(self,data):
        self.__data = data
        self.next = None
    def get_data(self):
        return self.__data


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

class LinkedList:
    def __init__(self):
        self.head=None  
    def display(self):
        temp = self.head
        while(temp.next != None):
            print(temp.get_data(),end=" ")
            temp = temp.next
        print(temp.get_data(),end=" ")
        print("\n")
    def insert_at_beginning(self,data):
        n = Node(data)
        n.next = self.head
        self.head=n
    def insert_between(self,data,node1):
        new_node=Node(data)
        temp = node1.next
        node1.next = new_node
        new_node.next = temp        
    def insert_at_end(self,data):
        n = Node(data)
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = n


        
ll=LinkedList()
ll.head=n1
ll.display()
ll.insert_at_beginning(1)
print("Beginning: ")
ll.display()
ll.insert_between(70,n4)
ll.display()
ll.insert_at_end(100)
ll.display()
