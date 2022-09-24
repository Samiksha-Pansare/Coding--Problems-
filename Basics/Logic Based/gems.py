#lex_auth_012693795044450304151

from operator import indexOf


def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    j=0
    for i in reqd_gems:
        if (i in gems_list):
            index_of_i= gems_list.index(i)
            price_of_i=price_list[index_of_i]
            bill_amount = bill_amount+(price_of_i*reqd_quantity[j])
            j=j+1
        else:
            return -1
    
    if(bill_amount>30000):
        percent_amt=(bill_amount*5)/100
        bill_amount=bill_amount-percent_amt
    #Write your logic here
    return bill_amount

#List of gems available in the store
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[1760,2119,1599,3920,3999]

#List of gems required by the customer
reqd_gems=["Ivory","Emerald","Garnet"]

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[3,10,12]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)
