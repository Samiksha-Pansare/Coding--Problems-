#lex_auth_0127136357122129921205
import math
def check_squares(number):
    for i in range(0,int(math.sqrt(number))): 
        rem=number - (i*i)
        print("Remainder: ",rem,"i: ",i)
        if math.sqrt(rem)-int(math.sqrt(rem))==0:
            return True
    return False
    #start writing your code here


number=61
print(check_squares(number))