class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        l = 0
        # Hum 'res' ya 'max_fruits' ki jagah seedhe window size use karenge
        for r in range(len(fruits)):
            # Update count
            count[fruits[r]] = count.get(fruits[r], 0) + 1
            
            # Agar 2 se zyada types ho gaye
            if len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
            
            # Hum window ko shrink nahi kar rahe, bas 'l' ko shift kar rahe hain
            # Isse window ki size humesha "ab tak ki maximum" rahegi
        
        return len(fruits) - l