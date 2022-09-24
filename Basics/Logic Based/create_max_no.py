#lex_auth_01269441913243238467

from unittest import result

from numpy import number


def create_largest_number(number_list):
    
    max_list=[]
    #remove pass and write your logic here
    for i in range(len(number_list)-1):
        #print(1)
        for j in range(0, len(number_list)-i-1):
            #print(2)
            if number_list[j] > number_list[j + 1]:
                #print(3)
                swapped = True
                number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]
    
    
    result=""
    #print("Number LIST",number_list)
    # print(max_list)
    for j in number_list:
        #print(j , type(j))
        result = str(j) + result
    
    return int(result)
            

        
            
        

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)