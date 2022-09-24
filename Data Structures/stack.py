from pyrsistent import v


class Stack:
    def __init__(self,size):
        self.__size=size
        self.__stack=[]
    def pop(self):
        if len(self.__stack)!=0:
            ele=self.__stack.pop()
            print(str(ele)+" is Popped!")
        else:
            print("Stack is empty!")
    def push(self,data):
        if len(self.__stack)<self.__size:
            self.__stack.append(data)
        else:
            print("Stack is Full!")
    def display(self):
        if len(self.__stack) != 0:
            for i in range(len(self.__stack),0):
                print(self.__stack[i])
        else:
            print("Stack is Empty!")

stk = Stack(5)
stk.push(10)
stk.push(15)
stk.push(20)
stk.push(25)
stk.push(30)
stk.push(35)
stk.display()
stk.pop()
stk.pop()
stk.pop()
stk.pop()
stk.pop()
stk.pop()


