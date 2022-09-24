class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1
    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False
    
    def is_empty(self):
        if(self.__top==-1):
            return True
        return False
    def push(self,data):
        if(self.is_full()):
            print("The stack is full!!")
        else:
            self.__top+=1
            self.__elements[self.__top]=data
    
    def pop(self):
        if(self.is_empty()):
            return -1
        else:
            data= self.__elements[self.__top]
            self.__top-=1
            return data

class Solution:
    def isValid(self, s: str) -> bool:
        openbrac=['(', '{', '[']
        closebrac=[')','}',']']
        og_stack=Stack(len(s))
        if (len(s)%2!=0):
            return False
        else:
            for i in range(0,len(s)):
                if s[i] in openbrac:
                    og_stack.push(s[i])
                elif s[i] in closebrac:
                    if og_stack.is_empty():
                        return False
                    elif (openbrac.index(og_stack.pop())==closebrac.index(s[i])):
                        continue
                    else:
                        return False
            if og_stack.is_empty():
                return True
            else:
                return False
                        
'''
19ms solution
class Solution:
    def isValid(self, s: str) -> bool:
                
        stack = []
        hash_table = {'(': ')',
                      '[': ']',
                      '{': '}'}
        
        for letter in s:
            if letter in hash_table:
                stack.append(letter)
            elif stack and letter == hash_table[stack[-1]]:
                stack.pop()
            else:
                return False
                
        valid = True if not stack else False
        return valid
'''
                
            
            
        