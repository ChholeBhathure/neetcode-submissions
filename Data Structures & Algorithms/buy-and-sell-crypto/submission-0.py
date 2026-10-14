class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum=prices[0]
        max_profit=0
        for i in prices:
            max_profit=max(max_profit,i-minimum)
            minimum=min(minimum,i)
        return max_profit
                
        
        