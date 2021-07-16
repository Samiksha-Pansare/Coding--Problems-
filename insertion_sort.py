'''
Teacher Took A Surprise Maths Test on Monday and only 5 students could score non-zero score and the maths 
teacher wants to find the runner-up among them
Give Input:
5
6 6 3 4 1
output: 
4
'''
def check_similar_score(score_list):
    for i in range(0,len(score_list)-1):
        n=score_list[i]
        if score_list.count(n)>1:
            score_list.remove(n)
    return score_list 
def runnerup(score_list,a):
    for j in range(0,a):
        key=score_list[j]
        i=j-1
        # here the condition should be i>-1
        while (i>-1) and (score_list[i]>key):
            score_list[i+1]=score_list[i]
            i=i-1
        score_list[i+1]=key
        #Indentation Of Return Statement was wrong 
        #and it is suppose to return the value a-2 instead of a-1
    return score_list[a-2]
if __name__ == '__main__':
    n = input()
    arr = map(int, input().split())
    score_list=list(arr)
    score_list=check_similar_score(score_list)
    b=runnerup(score_list,len(score_list))
    print(b)