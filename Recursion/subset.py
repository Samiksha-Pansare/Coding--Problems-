class Solution:
    def subsets(self, nums):
        allSubset = []
        def subsetfunc(ind,newset,arr,n,allSubset):
            if (ind==n):
                allSubset.append(newset)
                print("All Subset: ",allSubset)
                return
#                 Pick an element
            newset.append(arr[ind])
            print("Newset Picked: ",newset)
            
            subsetfunc(ind+1,newset,arr,n,allSubset)
#               Not Pick an element
            b = arr[ind]
            newset.remove(b)
            print("Newset not picked: ",newset)
            subsetfunc(ind+1,newset,arr,n,allSubset)
        print(nums)
        subsetfunc(0,[],nums,len(nums),allSubset)
        return allSubset

sol = Solution()
nums=[1,2,3]
res = sol.subsets(nums)
print(nums)
print(res)    
    
    
