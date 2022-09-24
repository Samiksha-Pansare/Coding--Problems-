#lex_auth_012694465248329728100

def validate_name(name):
    alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    name = name.lower()
    if (name!="" and len(name)<15):
        for letter in name:
            if letter in alpha:
                continue
            else:
                return False
        return True

def validate_phone_no(phno):
    nums=[0,1,2,3,4,5,6,7,8,9]
    first_num=phno[0]
    c=0
    if (len(phno)==10):
        for num in phno:
            if int(num) not in nums:
                return False
            if num == first_num:
                c=c+1
        if c==len(phno):
            return False
        return True
    

def validate_email_id(email_id):
    #Start writing your code here
    pass

def validate_all(name,phone_no,email_id):
    #Start writing your code here
    # Use the below given print statements to display appropriate messages
    # Also, do not modify them for verification to work
    #print("Invalid Name")
    #print("Invalid phone number")
    #print("Invalid email id")
    #print("All the details are valid")
    pass

#Provide different values for name, phone_no and email_id and test your program
validate_all("Tina", "9994599998", "tina@yahoo.com")