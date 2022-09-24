#lex_auth_01269446533799116898

from unittest import result


def check_perfect_number(number):
    factor_list=[]
    if(number==0):
        return False
    for i in range(1,number):
        if(number%i==0):
            factor_list.append(i)
    print("Number: ",number,factor_list)
    sum = 0 
    for num in factor_list:
        sum = sum + num
    print("'Sum: ",sum)
    if sum == number:
        return True
    return False
def check_perfectno_from_list(no_list):
    result=[]
    for n in no_list:
        if(check_perfect_number(n)):
            result.append(n)
    return result
        
perfectno_list=check_perfectno_from_list([87, 76, 567, 99, 0])
print(perfectno_list)