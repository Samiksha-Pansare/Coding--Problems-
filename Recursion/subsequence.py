from cgi import print_arguments


def subs(ind,s,n,arr):
    if(ind==n):
        for i in arr:
            print(i)
        if len(arr)==0:
            print("[]")
        return
    print("arr: ",arr,"n: ",n)
    print("s:",s,"ind: ",ind)
    # TAKE
    arr.append(s[ind])
    subs(ind+1,arr,n,arr)
    arr.pop()
    # NOT TAKE
    subs(ind+1,arr,n,arr)

s=[3,1,2]
n = len(s)
arr=[]
subs(0,s,n,arr)


