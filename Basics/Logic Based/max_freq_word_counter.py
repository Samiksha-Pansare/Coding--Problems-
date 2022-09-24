
def max_frequency_word_counter(data):
    word_count={}
    words=data.split(" ")
    for word in words:
        if word in word_count.keys():           
            word_count[word] = word_count.get(word) + 1
        else:
            word_count[word]=1;
    word = max(word_count, key=word_count.get)
    
    #start writing your code here
    #Populate the variables: word and frequency


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    print(word,word_count.get(word))


#Provide different values for data and test your program.
data="Rain on the green grass and Rain on the tree"
max_frequency_word_counter(data)