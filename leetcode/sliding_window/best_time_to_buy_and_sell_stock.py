def maxProfit(prices):
    '''
    prices[i] or actual value is the price of the coin on that day 
    we can choose a day to buy one coin and a day to sell it. 
    Days are in order, so we must buy before we sell.  
    '''
    max_profit = 0
    buy = prices[0]
    for price in prices:
        if price < buy: # we are trying to look for the smallest price so we can buy it, so we must set it. 
            buy = price
        else: 
            profit_today = price - buy 
            if profit_today > max_profit: 
                max_profit = profit_today

    return max_profit

# Program Flow 
# 1. max_profit = 0, buy = 7 
# 2. is 7 < 7 (price < buy)> no, lets go to the else block
# 3. profit_today = 7(price) - 7(buy) = 0 
        

print(maxProfit([7,1,5,3,6,0,12]))
                