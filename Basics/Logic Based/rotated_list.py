#lex_auth_0127136084107673601177

def rotate_list(input_list,n):
    output_list = input_list[-n:]
    print("Output List: ",output_list)
    for i in range(0,n):
        print("Input List: ",input_list)
        input_list.pop(-1)
        print("i: ",i)
    output_list=output_list+input_list
    #start writing your code here

    return output_list

input_list= [1,2,3,4,5,6]
output_list=rotate_list(input_list,2)
print(output_list)