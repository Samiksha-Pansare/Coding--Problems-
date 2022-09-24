#lex_auth_01269442545042227276

def find_ten_substring(num_str):

    # for digit in num_str:
    #     num = int(digit)
    #     if(sum+num<=10):
    #         sum = sum + digit
    results=[]
    for i in range(0,len(num_str)+1):
        for j in range(i+1,len(num_str)+1):
            print(num_str[i:j],"Num_Str")
            num = int(num_str[i:j])
            sum =0
            while (num>0):
                rem=num%10
                num = num//10
                sum = sum+rem
            print("Sum",sum)
            if (sum ==10):
                #print("10 Sum:",sum,i,j)
                results.append(num_str[i:j])
    
    return results
                
            
    #Remove pass and write your logic here

num_str="3523014"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)