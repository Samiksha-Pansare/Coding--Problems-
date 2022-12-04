class StackUsingResizableArray:
 
    def __init__(self):
        self.stack = [0]*1
        self.top = -1
 
    # // n is the capacity of the stack.
    # stack can hold at max n elements
    def push(self, data):
        if self.isFull():
            self.resize(2*len(self.stack))
        # as top index always points to last element in the stack,
        # increment top index by 1 and push the data
        self.top = self.top + 1
        self.stack[self.top] = data
 
    # // method to push data into stack
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")
        # always pop operation removes top/last element in the stack
        # decrement top index by 1
        topEle = self.stack[self.top]
        self.top = self.top-1
        return topEle
 
    # method to return top element from the stack
    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")
        return self.stack[self.top]
 
    # method to check overflow condition of the stack
    def isFull(self):
        return self.top+1 == len(self.stack)
 
    # method to check the stack is empty or not
    def isEmpty(self):
        return self.top == -1
 
    def resize(self, capacity):
        print("resizing stack capacity from  "+str(len(self.stack)) + " to " + str(capacity))
        tempStack = [0]*capacity
        for i in range(self.top+1):
            tempStack[i] = self.stack[i]
        self.stack = tempStack
 
    # method to print(stack data in LIFO order
    def printStack(self):
        for i in range(self.top+1):
            print(self.stack[i]),
        print("")
 
 
if __name__ == "__main__":
    obj = StackUsingResizableArray()
 
    for i in range(1, 10):
        obj.push(i*10)
        obj.printStack()
 
    print("Top Element Is ", obj.peek())
    print("POP Element Is ", obj.pop())
    print("Top Element After pop is ", obj.peek())