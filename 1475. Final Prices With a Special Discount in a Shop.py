class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        finalPrices, stack = list(prices), []      
        for i in range(len(prices) - 1, -1, -1):
            p = prices[i]
            while stack and p < stack[-1]:
                stack.pop()
            finalPrices[i] -= 0 if not stack else stack[-1]
            stack.append(p)
        return finalPrices
