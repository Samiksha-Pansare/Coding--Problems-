#lex_auth_012693782475948032141

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    #write your logic here
    if(quantity_ordered==0 or distance_in_kms<1):
        return -1;
    if(food_type=='N' or food_type=='V'):
        if (food_type=='N'):
            plate = 150*quantity_ordered;
            bill_amount=plate
            if(distance_in_kms>6):
                print(bill_amount)
                bill_amount=plate+(3*3)
                print(bill_amount)
                bill_amount=bill_amount+((distance_in_kms-6) * 6)
                print(bill_amount)
                return bill_amount
            elif(distance_in_kms>3):
                bill_amount=plate+((distance_in_kms-3) * 3) 
                return bill_amount
            else:
                return bill_amount
            
        elif(food_type=='V'):
            plate = 120*quantity_ordered;
            bill_amount=plate
            if(distance_in_kms>6):
                bill_amount=plate+(3*3)
                bill_amount=bill_amount+((distance_in_kms-6) * 6)
            elif(distance_in_kms>3):
                bill_amount=plate+((distance_in_kms-3) * 3) 
            else:
                return bill_amount
    else:
        return -1

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,0)
print(bill_amount)