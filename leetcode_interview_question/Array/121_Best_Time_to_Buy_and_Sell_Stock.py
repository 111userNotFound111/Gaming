"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

"""

def maxProfit(prices):
    # initialise a min price, 
    buy_price = prices[0]
    # initialise max profit, 
    max_profit = 0
    # record the day of purchase
    purchase_day = 0 
    
    # we look at the profitability 
    for day in range(0, len(prices)):
        if day != 0:
            # update purchase
            if prices[day] < prices[purchase_day]:
                print('buying')
                buy_price = prices[day]
                purchase_day = day
                print(buy_price)
            
            # update sell
            if prices[day] > buy_price:
                print('selling')
                max_profit = max_profit + (prices[day] - buy_price)
                # update min price after selling
                # set new default min price to current price
                buy_price = prices[day]
                purchase_day = day
        print(f'day {day}    buy price {buy_price}    profit {max_profit}')
    return max_profit
                
                
if __name__ == "__main__":
    # for [7,1,5,3,1,1,6], the answer should be 9
    prices = [7,6,4,3,1]
    print(maxProfit(prices))