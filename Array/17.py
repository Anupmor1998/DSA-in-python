# Best Time to Buy and Sell Stock

def maxProfit(prices):

    profit = 0
    i = 1
    buy = prices[0]

    while i < len(prices):
        buy = min(buy, prices[i])
        profit = max(profit, prices[i] - buy)
        i += 1
    return profit


print(maxProfit([7, 1, 3, 5, 6, 4]))
