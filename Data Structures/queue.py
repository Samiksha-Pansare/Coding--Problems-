from pyrsistent import v


class Queue:
    def __init__(self,size):
        self.__size=size
        self.__queue=[]
        self.__front =-1
        self.__rear = -1
    def dequeue(self):
        if self.__rear == self.__size-1:
            data=self.__queue[self.__front]
            print(data, "Dequeued!")
            self.__front=self.__front+1
        elif self.__rear==self.__front and len(self.__queue)==1:
            data=self.__queue[self.__front]
            print(data, "Dequeued!")
            self.__front=-1
            self.__rear=-1
        else:
            print("Queue is Empty!")


        if len(self.__queue)!=0:
            ele=self.__queue.pop(self.__front)
            print(str(ele)+" is Dequeued!")
            self.__front=self.__front+1
        elif(self.__front==self.__rear):
            print("Queue is empty!")
    def enqueue(self,data):
        if (len(self.__queue)==0):
            self.__queue.append(data)
            self.__front+=1
            self.__rear+=1
            print(data," is Enqueued!")
        elif (len(self.__queue)>0) and (len(self.__queue)<self.__size):
            self.__queue.append(data)
            self.__rear=self.__rear+1
        else:
            print("Queue is Full!")
            print(data," is Enqueued!")
    def display(self):
        if len(self.__queue) != 0:
            for data in self.__queue:
                print(data)
        else:
            print("Queue is Empty!")

que = Queue(5)
que.enqueue(10)
que.enqueue(15)
que.enqueue(20)
que.enqueue(25)
que.enqueue(30)
que.enqueue(35)
que.display()
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()


