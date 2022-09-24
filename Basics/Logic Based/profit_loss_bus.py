#lex_auth_012693816779112448160

from cmath import cos
import profile


def calculate(distance,no_of_passengers):
    fuel_reqd=distance*70
    cost=fuel_reqd/10
    print("Cost:", cost)
    revenue=no_of_passengers*80
    print("Revenue:", revenue)
    profit = revenue - cost
    print("Profit:", profit)
    if profit>0:
        return profit
    else:
        return -1
    



#Provide different values for distance, no_of_passenger and test your program
distance=100
no_of_passengers=10
print(calculate(distance,no_of_passengers))