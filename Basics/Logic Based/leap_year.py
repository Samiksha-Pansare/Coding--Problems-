#lex_auth_012693797166096384149

def find_leap_years(given_year):
    list_of_leap_years=[]
    for i in range(given_year,given_year+64):
        if(len(list_of_leap_years)==15):
            break
        elif(i%100 == 0 and i%400 == 0):
            list_of_leap_years.append(i)
        elif(i%4==0 and i%100!=0):
            list_of_leap_years.append(i)
        
            
        
    # Write your logic here

    return list_of_leap_years

list_of_leap_years=find_leap_years(2000)
print(list_of_leap_years)