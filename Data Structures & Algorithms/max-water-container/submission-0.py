class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        for i in range (len(heights)):
            for j in range(i+1,len(heights)):
                amount = (j-i)*min(heights[i], heights[j])
                if amount>max:
                    max = amount
        return max
        