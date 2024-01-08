prices = [7,1,5,3,6,4]

def maxProfit(prices):
    TotalProfit = 0

    for price in range(len(prices) - 1):
        if prices[price + 1] > prices[price] :
            profit =  prices[price + 1] -  prices[price]
            print(profit)
            TotalProfit = TotalProfit + profit
    return TotalProfit


    
print(maxProfit(prices))