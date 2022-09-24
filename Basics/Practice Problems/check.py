'''
Problem Statement
Write a python function which accepts three numbers and returns True if

a. one of the three numbers is "close" to any one of the other numbers (differing from a number by at most 1), and

b.Number that is left out is "far", differing from both other values by 2 or more.

Return false if the above mentioned conditions are not satisfied

i/p: 4,1,3
o/p: True

i/p: 5,6,7
o/p: False
'''
#lex_auth_0127136008767324161169

def close_number(num1,num2,num3):
    if (abs(num1-num2)<=1 or abs(num2-num3)<=1 or abs(num3-num1)<=1):
        if(abs(num1-num2)>=2 or abs(num2-num3)>=2 or abs(num3-num2)>=2):
            return True
    return False
print(close_number(5,4,2))