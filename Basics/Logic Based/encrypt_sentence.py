#lex_auth_01269444195664691284
def encrypt_sentence(sentence):
    words = sentence.split(" ")
    new_sentence=[]
    for i in range(1,len(words)+1):
        #print(sentence[i])
        if(i%2!=0):
            word=words[i-1]
            word= word[::-1]
            words[i-1] = word
            #print(word,i)
        else:
            vowels=['A','E','I','O','U','a','e','i','o','u']
            temp=[]
            for letter in words[i-1]:
                if letter in vowels:
                    temp.append(letter)
                    words[i-1]=words[i-1].replace(letter,'')
                #print("Temp:",temp)
            for letr in temp:
                words[i-1]=words[i-1]+letr
                #print("Vowel Letters",words[i-1])
                #print("Vowel Letters:",temp)
            #print("Remove Vowels",words)
    #print(words)
    new_sentence=''
    for word in words:
        new_sentence = new_sentence +  word + " "
    print(new_sentence)
    new_sentence=new_sentence.replace('"','')
    new_sentence=''
    for word in words[0:len(words)-1]:
        new_sentence = new_sentence +  word + " "
    new_sentence = new_sentence + words[len(words)-1]
    return new_sentence

sentence="She sells sea shells on the sea shore"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)