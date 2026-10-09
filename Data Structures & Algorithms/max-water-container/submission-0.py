class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maximum=0
        while left<right:
            width=right-left
            area=(min(heights[right],heights[left]))*width
            maximum=max(area,maximum)
            if heights[left]<=heights[right]:
                left+=1
            elif heights[left]>heights[right]:
                right-=1
        return maximum    
