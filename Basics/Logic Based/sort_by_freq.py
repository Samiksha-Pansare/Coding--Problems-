class Solution:
    def frequencySort(self, s: str) -> str:
        char_count = {}
        for c in s:
            if c in char_count:
                char_count[c] = char_count[c] + 1
            else:
                char_count[c] = 1
        print("Charcter Dictionary: ",char_count)
        sorted_s = sorted(char_count.items(), key=lambda x:x[1],reverse=True)
        print("Sorted String: ",sorted_s)
        res=""
        for i in sorted_s:
            res = res+ i[0] * i[1]
            print("i: ",i)
        return res
        

sol=Solution()
s="Aabb"
print(sol.frequencySort(s))
print("i"*2)