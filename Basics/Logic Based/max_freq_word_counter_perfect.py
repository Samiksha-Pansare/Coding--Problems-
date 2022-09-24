def max_frequency_word_counter(data):
    word=""
    frequency=0
    lower_data=data.lower()
    lst=[]
    lst=lower_data.split()
    repeat=[]
    a=[]
    i=0
    while(i < len(lst)):
        if lst.count(lst[i]) > 1:
            repeat.append(lst[i])
            i=i+1
        else:
            i=i+1
    for i in repeat:
        a=repeat.count(i)
    
    for i in range(0,len(repeat)):
        if repeat.count(repeat[i])==a:
            word=word+repeat[i]
            frequency=a
            break
    print(word,frequency)