#lex_auth_012693810762121216155

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0

    if (legs%2==0):    
        rabbit_count=(legs//2) - heads
        chicken_count =heads- rabbit_count
        if(rabbit_count>0 and chicken_count>0):
            print(int(chicken_count),int(rabbit_count))
    else:
        print(error_msg)
    

    # if(type(chicken_count)==int and type(rabbit_count)==int ):
    #     print(chicken_count,rabbit_count)
    # else:
    #     print(error_msg)
    

    #Start writing your code here
    
    #Populate the variables: chicken_count and rabbit_count



    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    
    #print(error_msg)

#Provide different values for heads and legs and test your program
solve(35,94)