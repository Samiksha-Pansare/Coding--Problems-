def nextPermutation(nums=[1,5,8,4,7,6,5,3,1]):
    print("Inside")
    print("Nums: ", nums)
    print("Len: ", len(nums))
    idx = -1
    for i in range(len(nums)-1,0,-1):
        if nums[i]>nums[i-1]:
            idx=i
            break
    print("IDX: ",idx,"nums[idx]: ",nums[idx])
    if idx == -1:
        nums.reverse()
    else:
        prev=idx
        for i in range(idx+1,len(nums)):
            if nums[i]>nums[idx-1] and nums[i]<=nums[prev]:
                prev = i
                print("Prev: ",prev,"nums[prev]: ",nums[prev])
        a=nums[idx-1]
        nums[idx-1]=nums[prev]
        nums[prev]=a
        #nums[idx-1], nums[prev] = nums[prev], nums[idx-1]
        temp = nums[idx:len(nums)]
        print("Temporary Array: ",temp)
        temp = temp[::-1]
        nums=nums[0:idx]+temp
        print("Rev Temp Array: ",temp)
    print("Final Nums: ", nums)

print(nextPermutation([1,5,8,4,7,6,5,3,1]))
print("Outside")
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums)-1
        while i>0:
            if nums[i-1]<nums[i]:
                break
            i = i-1
        i = i-1
        j = len(nums)-1
        while j>i:
            if nums[j]>nums[i]:
                break
            j=j-1
        nums[i],nums[j]=nums[j],nums[i]  
        nums[i+1:]=sorted(nums[i+1:])
'''
                    
                    
                    

        