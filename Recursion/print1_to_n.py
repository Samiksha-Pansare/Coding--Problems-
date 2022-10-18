def printn(n,i=1):
    if (i==n):
        print(i)
        return
    else:
        print(i,end=" ")
        printn(n,i+1)


printn(5)

# Descending

def printn(n,i=1):
    if (i>n):
        return
    else:
        printn(n,i+1)
        print(i,end=" ")


printn(5)