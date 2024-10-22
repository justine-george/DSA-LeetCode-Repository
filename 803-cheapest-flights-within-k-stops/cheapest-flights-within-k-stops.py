class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k + 1):
            tempPrices = prices.copy()
            # isChanged = False
            
            for fromStop, toStop, price in flights:
                if prices[fromStop] == float('inf'):
                    continue
                if price + prices[fromStop] <= tempPrices[toStop]:
                    tempPrices[toStop] = price + prices[fromStop]
                    # isChanged = True
            
            # if not isChanged:
            #     break
            prices = tempPrices
        
        return prices[dst] if prices[dst] != float('inf') else -1