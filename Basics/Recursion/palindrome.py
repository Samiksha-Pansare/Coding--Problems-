#lex_auth_01269442114344550475

def is_palindrome(word):
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
        return is_palindrome(word[1:len(word)-1]) 
    return False   
     
    #Remove pass and write your logic here

#Provide different values for word and test your program
result=is_palindrome("A man, a plan, a canal: Panama")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")