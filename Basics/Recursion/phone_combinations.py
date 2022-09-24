class Solution:
    def solve(self, digits: str,output: list,index: int,ans: list,mapping: list):
        if (index >= len(digits)):
            ans.append(output)
            return
        number = ord(digits[index]) - ord('0')
        value = mapping[number]
        for i in range(0,len(value)):
            output.append(value[i])
            self.solve(digits,output,index+1,ans,mapping)
            output.pop()
    def letterCombinations(self, digits: str):
        ans =[]
        if len(digits)==0:
            return ans
        output = []
        index = 0
        mapping =["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        self.solve(digits,output,index,ans,mapping);
        return ans
sol = Solution
        
print(sol.letterCombinations("23"))