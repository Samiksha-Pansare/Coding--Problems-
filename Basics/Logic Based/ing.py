#lex_auth_0127135929511936001157

def calculate_net_amount(trans_list):
    trans_dict={}
    for i in trans_list:
        transaction = i[0:1]
        print("i: ",i)
        if transaction in trans_dict:
            print(transaction)
            trans_dict[transaction]+=int(i[2:])
        else:
            print(transaction)
            trans_dict[transaction]=+int(i[2:])

    net=0 
    for trans in trans_dict:
        if trans=="D":
            net=net+trans_dict[trans]
        else:
            net = net - trans_dict[trans]
    #start writing your code here
    print("Dictionary: ",trans_dict)
    return net

trans_list=["D:300","D:200","W:200","D:100"]
print(calculate_net_amount(trans_list))