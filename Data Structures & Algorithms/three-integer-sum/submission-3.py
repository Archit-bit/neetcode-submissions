class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res=[]

        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l,r=i+1,n-1
            target = -nums[i]
            while l<r:
                
                s= nums[l]+nums[r]
                if target==s:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                        continue
                        
                if target<s:
                    r -=1
                if target>s:
                    l+=1
                
        return res


            

            
        