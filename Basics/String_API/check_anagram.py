#lex_auth_0127382206342184961397

def check_anagram(data1,data2):
    data1,data2=data1.lower(),data2.lower()
    if(sorted(data1)==sorted(data2)):
        for i in range(0,len(data1)):
            if (data1[i] == data2[i]):
                return False
        return True
    return False

print(check_anagram("eat","tea"))
'''
19ms Fastest Solution
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return all(s.count(i) == t.count(i) for i in string.ascii_lowercase)
'''