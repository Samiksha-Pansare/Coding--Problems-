class Solution:
    def bestClosingTime(self, customers):
        # penalty_dict={}
        # Approach 1
        # for i in range(0,len(customers)+1):
        #     penalty_dict[i]=0
        #     for j in range(0,len(customers)):
        #         if ((j<i) and customers[j]=="N"):
        #             penalty_dict[i] = penalty_dict[i]+1
        #         elif ((j>=i) and customers[j]=="Y"):
        #             penalty_dict[i] = penalty_dict[i]+1

        # Approach 2
        # for i in range(0,len(customers)+1):
        #     before = customers[0:i]
        #     after=customers[i:len(customers)]
        #     bef = before.count("N")
        #     aft = after.count("Y")
        #     penalty_dict[i]=bef+aft
            

        # res =  min(penalty_dict, key=lambda k: penalty_dict[k]) 
        # print(customers)
        # print("Penalty dict: ",penalty_dict)
        # print("res: ",res)
        # return res
        # Most optimal
        n = len(customers)
        penalty = customers.count('Y')
        if penalty == n: 
            return n
        min_, ans = n, 0
        for index, value in enumerate(customers):
            if min_ > penalty:
                min_ = penalty
                ans = index
            if value == 'Y':
                penalty -= 1
            else:
                penalty += 1
        if min_ > penalty: return n
        return ans

customers="YYNY"
sol =Solution()
print(sol.bestClosingTime(customers))