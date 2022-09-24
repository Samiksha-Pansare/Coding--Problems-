#lex_auth_01269444890062848087

from numpy import correlate


def find_correct(word_dict):
    correct_word_count=0
    almost_correct=0
    wrong=0
    for ques,ans in word_dict.items():
        diff_char = 0
        x=len(ques) if len(ques)<len(ans) else len(ans)
        print(x,"x")
        if(ques==ans):
            correct_word_count=correct_word_count+1
            print("Correct Word: ",ques,ans)
        else:
            for i in range(0,x):
                if ques[i]!=ans[i]:
                    diff_char = diff_char+1
                diff_char = diff_char + abs(len(ques)-len(ans))
                
            if(diff_char<=2 and diff_char):
                almost_correct = almost_correct+1
                print("Almost Correct Word: ",ques,ans)
            else:
                wrong = wrong+1
                print("Wrong Word: ",ques,ans)
    return [correct_word_count,almost_correct,wrong]
    #start writing your code here

word_dict={'MIND': 'MUND', 'CHECK': 'CHEK', 'ALWAYS': 'ALLISWELL', 'VENDOR': 'VENDING', 'RADIO': 'RADICAL'}
print(find_correct(word_dict))