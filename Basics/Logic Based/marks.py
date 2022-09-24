#lex_auth_01269438947391897654

#Global variable
from itertools import count


list_of_marks=[12,18,25,24,2,5,18,20,20,21]

def find_more_than_average():
    sum = 0
    count=0
    for marks in list_of_marks:
        sum = sum+marks
    avg = sum/(len(list_of_marks)+1)
    for marks in list_of_marks:
        if marks > avg:
            count=count+1
    return count

def sort_marks():
    for i in range(0,len(list_of_marks)):
        for j in range(i+1,len(list_of_marks)):
            if list_of_marks[i]>list_of_marks[j]:
                temp = list_of_marks[j]
                list_of_marks[j]=list_of_marks[i]
                list_of_marks[i]=temp
    return list_of_marks
    #Remove pass and write your logic here

def generate_frequency():
    freq=[]
    for i in range(0,len(list_of_marks)):
        count =0
        for j in range(i+1,len(list_of_marks)):
            if list_of_marks[i] == list_of_marks[j]:
                count=count+1

        freq.append(count)
    return freq

            

    
    #Remove pass and write your logic here


print(find_more_than_average())
print(generate_frequency())
print(sort_marks())