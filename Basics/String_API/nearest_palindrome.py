#lex_auth_01269443664174284882
def nearest_palindrome(number):
    number = number+1
    while True:        
        if is_palindrome(number):
            return number
        else:
            number = number+1
    pass
    #start writitng your code here
def is_palindrome(word):
    word = str(word)
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

number=99
print(number)
print(nearest_palindrome(number))