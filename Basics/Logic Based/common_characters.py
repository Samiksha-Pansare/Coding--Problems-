#lex_auth_012693825794351104168

from unittest import result


def find_common_characters(msg1,msg2):
    result=""
    for i in msg1:
        if(i not in msg2):
            pass
        else:
            if(i!=" " and i not in result):
                result = result+i
            else:
                pass
    if result=="":
        return -1
    return result
#Provide different values for msg1,msg2 and test your program
msg1="moto"
msg2="moto"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)