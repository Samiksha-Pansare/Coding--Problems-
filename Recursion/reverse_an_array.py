def func(l,r,arr):
    if(l>=r):
        print(arr)
        return arr
    else:
        arr[l],arr[r]=arr[r],arr[l]
        print("here",arr[l],arr[r])
        func(l+1,r-1,arr)
res = func(0,4,[1,2,3,4,5])
print(res)