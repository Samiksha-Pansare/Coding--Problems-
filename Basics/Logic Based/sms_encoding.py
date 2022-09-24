#lex_auth_01269444961482342489

def sms_encoding(data):
    words=data.split(" ")
    # print(words)
    # print(words[0],": First ",words[1],": Second",words[2]," : Third")
    vowels=['A','E','I','O','U','a','e','i','o','u']
    for i in range(1,len(words)+1):
        temp = words[i-1]
        for letter in words[i-1]:
            if letter in vowels:
                words[i-1] = words[i-1].replace(letter,"")
        if words[i-1]=="":
            words[i-1] = temp         
    new_sentence=''
    for word in words[0:len(words)-1]:
        new_sentence = new_sentence +  word + " "
    new_sentence = new_sentence + words[len(words)-1]
    return new_sentence      
    #start writing your code here

data="I love Python"
print(sms_encoding(data))