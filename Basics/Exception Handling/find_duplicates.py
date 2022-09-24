#lex_auth_01269443477535129681

from os import dup


def find_duplicates(list_of_numbers):
    duplicate=[]
    i=0
    for num in list_of_numbers:
        if (list_of_numbers.count(num)>1) and num not in duplicate:
            duplicate.append(num)
    return duplicate       
    #start writing your code here

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)