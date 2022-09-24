from hashlib import new
from Basics.Recursion.palindrome import is_palindrome


class Solution:
    def is_palindrome(self,word):
        word = word.lower()
        word = word.strip()
        print(word)
        i = 0
        j = len(word)-1
        if(len(word)<=1):
            return True
        if(word[i]==word[j]):
            print("i: ",i,"j: ",j)
            i=i+1
            j=j-1
            return self.is_palindrome(word[1:len(word)-1]) 
        return False 
   
                
