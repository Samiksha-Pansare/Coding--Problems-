'''
10
5 5 5 5 5 5 5 5 5 6

def check_similar_score(score_list):
    c=0
    repeated_ele=[]
    for i in score_list:
        n=i
        c=c+1
        print(n)
        if score_list.count(n)>1:
            repeated_ele.append(n)
    rem_ele=score_list-repeated_ele
    final_list=rem_ele.sort()
    print(final_list)    
    return final_list 
'''
def Remove(score_list):
    final_list = []
    for num in score_list:
        if num not in final_list:
            final_list.append(num)
    print(final_list)
    return final_list 
if __name__ == '__main__':
    a = input()
    n=int(a)
    if 2<=n<=10:
        arr = map(int, input().split())
        score_list=list(arr)
        score_list.sort()
        for i in score_list:
            if -100<i<100:
                break
        new_list=Remove(score_list)
        if len(new_list)==1:
            print(new_list[0])
        else:
            print(new_list[len(new_list)-2])