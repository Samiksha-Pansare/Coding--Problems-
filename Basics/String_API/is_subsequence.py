class Solution:
    def isSubsequence(s: str, t: str) -> bool:
        indexlist = []
        for letter in s:
            if letter in t:
                indexlist.append(t.index(letter))
                print(t.index(letter))
            else:
                return False
        temp = indexlist
        print(temp)
        indexlist.sort()
        print(indexlist)
        if temp == indexlist:
            return True
        else:
            return False

print(Solution.isSubsequence("acb","ahbgdc"))