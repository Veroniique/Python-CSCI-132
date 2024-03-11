'''
7 March 2024
Objective: Stock Market simulator. Tells user to buy, sell, stocks.
           Monitors their portfolio, traces historical prices of
           a set of stocks.
TODO: - Show history of price(s)
    - Create a quantity list to show shares owned by user and all previous purchases
    - Create functions: - transactions
                        - record transaction
                        - random walk for adjusting stock prices after transaction
    - Save user data
    - Add error handling
    - Include strtlower on all inputs!!! (validation)
'''
#imported libraries
import random

#user money
user_money = 15000

#stock dictionary with name and price list
stock_data = {}

while True:
    # user prompts
    print("Welcome to the Stock simulator\n")
    print("1. Display stocks")
    print("2. Purchase stocks")
    print("3. Sell stocks")
    print("4. Observe portfolio")
    print("5. Save portfolio")
    print("6. Exit\n")
    user_input = int(input("Choose a number between 1 - 6: "))

    #Task 1.3 - Show stock name + price
    if user_input == 1:
        for stock, price in stock_data.items():
            print(f"The price of {stock} stock is ${price}")

    #Task 2 - Open stock.txt file to read data
    with open('stock.txt', 'r') as file:
        #read each line
        for line in file:
            #split data in stock name and stock price
            stock_name, initial_price = line.strip().split(',')

            #store stock data in dictionary
            if stock_name not in stock_data:
                stock_data[stock_name] = {'price': float(initial_price), 'quantity': 0}

    #Show stored data
    print("Stock Data: ")
    for stock, data in stock_data.items():
        print(f"{stock}: {data['price']}")

    #Task 3 - Function to buy stock
    def buy_stock(stock_data, stock_name, share_amount, user_money):
        if stock_name not in stock_data:
            print(f"{stock_name} does not exist")
            return user_money

        #cost calculations for buying stocks
        stock_price = stock_data[stock_name]['price']
        total_cost = stock_price * share_amount

        #check if user has enough money
        if total_cost > user_money:
            print("You don't have enough money to buy this stock")
            return user_money

        #deduct money from user funds
        user_money -= total_cost

        #update user's stock when changes are made
        stock_data[stock_name]['quantity'] += share_amount

        #display how much bought of stock by price and total remaining
        print(f"You have bought {share_amount} of {stock_name} for {stock_price} per share")
        print(f"Your remaining total: {user_money}")

        return user_money

    #Task 3.1 - Calling function buy stock
    if user_input == 2:
        stock_name = (input("What stock do you want to buy: "))
        share_amount = int(input(f"How much of {stock_name} do you want to buy: "))

        #calling function buy_stock
        user_money = buy_stock(stock_data, stock_name, share_amount, user_money)

    #Task 4 - Function to sell stock
    def sell_stock(stock_data, stock_name, share_amount, user_money):
        if stock_name not in stock_data:
            print(f"{stock_name} does not exist")
            return user_money

        if stock_data[stock_name]['quantity'] >= share_amount:
            stock_price = stock_data[stock_name]['price']
            total_earned = stock_price * share_amount

            #Add money to user funds
            user_money += total_earned

            #update user stock
            stock_data[stock_name]['quantity'] -= share_amount

            print(f"you have sold {share_amount} of {stock_name} for {stock_price} per share.")
            print(f"Total earnings: {total_earned}")
            print(f"Your Remaining total: {user_money}")
        else:
            print(f"You don't have enough shares of {stock_name} to sell at this time.")

        return user_money

    #Task 4.1 - Calling function sell stock
    if user_input == 3:
        stock_name = input(f"What stock do you want to sell? ")
        share_amount = int(input(f"How much of {stock_name} do you want to sell? "))

        #calling function sell stock
        user_money = sell_stock(stock_data, stock_name, share_amount, user_money)

    #Task 5 - View user stocks
    def view_stocks(stock_data):
        print("Your portfolio results: ")
        total_portfolio_value = 0
        for stock, data in stock_data.items():
            #filter out stocks that are greater 0
            quantity = data['quantity']
            if quantity > 0:
                price = data['price']
                total_value = quantity * price
                #gets user total portfolio value
                print(f"{stock} - Quantity: {quantity}, Total value: {total_value}")
                total_portfolio_value += total_value

        print(f"Total portfolio value: {total_portfolio_value}")

    if user_input == 4:
        view_stocks(stock_data)

    #Task 6 - Save user stocks
    #def save_stocks():
        #if user_input == 5:


    #Task 7 - Exit message
    if user_input == 6:
        print("Thank you for checking the Stock Market today!")
        break

    '''
    #function example for creating prices
    def simulate_price_change(current_price):
        ###add 3 ' here
        Simulate a random price change for a stock.
    
        :param current_price:
        current_price(float): The current price of the stock.
    
        :return:
        float: The new price after the random walk.
        ###add 3 ' here
        # Define parameters for the random walk
        drift = 0.2 #Avg annual return (can be adjusted)
        volatility = 0.3 #Volatility (can be adjusted)
    
        # Generate a random change based on a normal distribution
        random_change = random.gauss(drift, volatility)
    
        # Apply the random change to the current price
        new_price = current_price * (1 + random_change)
    
        # Ensure the new price is not negative
        if new_price < 0.01:
            new_price = 0.01
    
        return new_price
    
        # Example usage:
        current_price = 100.0 #Replace with the actual current price
        new_price = simulate_price_change(current_price)
        print(f"New price: ${new_price:.2f}")
    '''
