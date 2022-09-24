#lex_auth_012693813706604544157

def find_max(num1, num2):
    max_num=-1
    max_num=-1
    result=[]
    if(num1<num2):
        for i in range(num1,num2+1):
            num = i
            sum =0
            digit =0
            while(num>0):
                remainder = num%10
                sum = sum + remainder
                num = num//10
                digit = digit +1
            if(sum%3==0 and i%5==0 and  digit==2):
                result.append(i)
    
        max_num=-1
        for j in result:
            if j > max_num:
                max_num=j

        return max_num
    else:
        return -1

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,15)
print(max_num)