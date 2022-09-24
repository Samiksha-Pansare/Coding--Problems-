#lex_auth_0127382164803993601239

#This verification is based on string match.

def sum_of_numbers(list_of_num,filter_func=None):
    if filter_func==even:
        even_list=even(list_of_num)
        sum =0
        for num in even_list:
            sum = sum + num
        return sum
    elif filter_func==odd:
        odd_list=odd(list_of_num)
        sum =0
        for num in odd_list:
            sum = sum + num
        return sum
    else:
        sum =0
        for num in list_of_num:
            sum = sum + num
        return sum

def even(data):
    even_list=[]
    for num in data:
        if(num%2==0):
            even_list.append(num)
    return even_list

def odd(data):
    odd_list=[]
    for num in data:
        if(num%2!=0):
            odd_list.append(num)
    return odd_list

sample_data = range(1,11)

print(sum_of_numbers(sample_data,None))