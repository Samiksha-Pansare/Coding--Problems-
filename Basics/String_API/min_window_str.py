# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# A substring is a contiguous sequence of characters within the string.


def minWindow(s, t):
    str_arr=list(s)
    print("String Array: ",str_arr)
    req_arr=list(t)
    for i in range(0,len(t)):
        if t[i] not in str_arr:
            print("i here")
            return ""
    print("Before while loop")
    l=0
    r=len(s)-1
    while len(str_arr)>len(req_arr):
        str_arr=str_arr[l+1:r]
        print("Crop",str_arr)
        for i in range(0,len(t)):
            if t[i] not in str_arr:
                return s[l:r+1]
        l=l+1
        r=r-1
    return s[l:r]


print(minWindow("ADOBECODEBANC","ABC"))