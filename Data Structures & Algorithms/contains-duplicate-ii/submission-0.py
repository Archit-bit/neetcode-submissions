class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window_set=set()
        for right in range(len(nums)):
            if nums[right] in window_set:
                return True
            window_set.add(nums[right])
            if len(window_set)>k:
                window_set.remove(nums[right-k])
        return False
          
        