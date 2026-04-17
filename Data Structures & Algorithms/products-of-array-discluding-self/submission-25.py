class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1
        s=1
        prefix=[]
        suffix=[]
        for i in range(len(nums)):
            if i==0:
                prefix.append(p)
            else:
                p*=nums[i-1]
                prefix.append(p)
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                suffix.append(s)
            else:
                s*=nums[i+1]
                suffix.append(s)
        suffix.reverse()
        return[x*y for x,y in zip(prefix,suffix)]



        