
def check(s,l,r) -> bool:
    print(l)
    print(r)
    if (l>=r):
        print(True)
        return True
    else:
        if s[l] != s[r]:
            print(s[l])
            print(s[r])
            print(False)
            return False
        check(s,l+1,r-1)
        
def isPalindrome(x: int) -> bool:
    s = [int(i) for i in str(x)]
    print(s)
    l=0
    r = len(s)-1
    check(s,l,r)

print(isPalindrome(121))