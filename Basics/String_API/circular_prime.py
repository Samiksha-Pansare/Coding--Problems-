#lex_auth_01269446157664256093

def check_prime(number):
    if number==2:
        return True
    elif number<2:
        return False
    else:
        for i in range(2,number):
            if number%i==0:
                return False
    return True

def rotations(num):
    answer = [num]
    digits=len(str(num))
    for i in range(digits-1):
        if(len(str(num))<digits):
            e = num*10
        else:
            a=num*10
            b=int(str(num)[0])
            c=a+b
            d=b*(pow(10,digits))
            e=c-d
        answer.append(e)
        num=e
    return answer

    pass #remove pass and write your logic here. It should return the list of different combinations of digits of the given number.
	#Rotation should be done in clockwise direction. For example, if the given number is 197, the list returned should be [197, 971, 719]

def get_circular_prime_count(limit):
    c=0
    for i in range(2,limit):
        if check_prime(i):
            d=0
            rotlist=rotations(i)
            for j in rotlist:
                if check_prime(j):
                    d=d+1
            if d==len(str(i)):
                c=c+1   
    return c