def stock(prices): 
    max_profit = 0 
    buy = prices[0]

    for price in prices: 
        if price < buy: 
            buy = price 
        else: 
            price_today = price - buy
            if price_today > max_profit: 
                max_profit = price_today
    
    return max_profit




print(stock([7, 1, 5, 3, 6, 4]))