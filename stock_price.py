sp = [7,10,5,3,6,4,1]

def func(stock_price):

    buying_price = stock_price[0]
    profit = 0

    for i in range(1, len(stock_price)):
        if buying_price > stock_price[i]:
            buying_price = stock_price[i]
        
        elif stock_price[i] - buying_price > profit:
            profit = stock_price[i] - buying_price
    
    return profit

print(func(sp))
