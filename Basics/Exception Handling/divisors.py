#lex_auth_01269442760027340879
def find_factors_len(num):
    factor_list=[]
    for i in range(1,num+1):
        if(num%i==0):
            factor_list.append(i)
    print(factor_list)
    return len(factor_list)
def find_smallest_number(num):
    c=1
    while(True):
        if(find_factors_len(c)==num):
            return c
        c=c+1
    return -1


num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)