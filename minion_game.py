def minion_game(string):
    # your code goes here
    if 0<len(s)<10**6:
        test_str=str.upper(s)
        vowels=['A','E','I','O','U']
        player1 = 'Kevin'
        player2 = 'Stuart'
        player1score=[]
        player2score=[] 
        res = [test_str[i: j] for i in range(len(test_str)) 
            for j in range(i + 1, len(test_str) + 1)]
        for word in res:
            if word[0] in vowels:
                player1score.append(word)
            else:
                player2score.append(word)
        if  len(player1score)>len(player2score):
            print("{} {}".format(player1,len(player1score)))
        elif  len(player1score)==len(player2score):
            print("{}".format("Draw"))
        
        else:
            print("{} {}".format(player2,len(player2score)))  

if __name__ == '__main__':
    s = input()
    minion_game(s)