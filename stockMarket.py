'''
7 March 2024
Objective: Stock Market simulator. Tells user to buy, sell, stocks.
           Monitors their portfolio, traces historical prices of
           a set of stocks.
TODO: -Incorporate random walk function for random simulation of prices
    - Include strtlower on all inputs!!! (validation)
'''

#imported libraries
import random

#user money
user_money = 15000

#Function that loads up the user portfolio
def load_portfolio():
    portfolio = {}
    try:
        with open('user_portfolio.txt', 'r') as file:
            for line in file:
                stock_name, quantity, total_cost = line.strip().split(',')
                portfolio[stock_name] = {'quantity': int(quantity), 'total_cost': float(total_cost)}
    except FileNotFoundError:
        print("User portfolio.txt not found")
    except ValueError:
        print("Incorrect Data")

    return portfolio

#Function that saves user stock info to external txt sheet
def save_portfolio(portfolio):
    with open('user_portfolio.txt', 'w') as file:
        for stock, data in portfolio.items():
            file.write(f"{stock},{data['quantity']},{data['total_cost']}\n")

#Load user portfolio from file
user_portfolio = load_portfolio()

#Loads up the stock file with current stock and prices
def load_stockdata():
    #Empty dict
    stock_data = {}
    # Task 2 - Open stock.txt file to read data
    with open('stock.txt', 'r') as file:
        # read each line
        for line in file:
            # split data in stock name and stock price
            stock_name, initial_price = line.strip().split(',')

            # store stock data in dictionary
            stock_data[stock_name] = float(initial_price)

    return stock_data

#Function that allows user to buy stock
def buy_stock(stock_data, stock_name, share_amount, user_money, user_portfolio):
    #check if stock exists in stock data
    if stock_name in stock_data:
        #gets price of stock
        stock_price = stock_data[stock_name]

        # cost calculations for buying stocks
        total_cost = stock_price * share_amount

        # check if user has enough money
        if total_cost <= user_money:
            #deduct money from user funds
            user_money -= total_cost
            if stock_name in user_portfolio:
                # update user portfolio
                user_portfolio[stock_name]['quantity'] += share_amount
                user_portfolio[stock_name]['total_cost'] += total_cost
            else:
                user_portfolio[stock_name] = {'quantity': share_amount, 'total_cost': total_cost}
            # display how much bought of stock by price and total remaining
            print(f"You have bought {share_amount} of {stock_name} for {stock_price} per share")
            print(f"Total cost: ${total_cost}")
            print(f"Your remaining total: ${user_money}")
        else:
            print("You don't have enough money to buy this")
    else:
        print("Stock not found in the stock data.")

    return user_money, user_portfolio

# Function that allows user to sell their stock(s)
def sell_stock(stock_data, stock_name, share_amount, user_money, user_portfolio):
    #check if stock exists in user_portfolio
    if stock_name in user_portfolio:
        if user_portfolio[stock_name]['quantity'] >= share_amount:
            if stock_name in stock_data:
                stock_price = stock_data[stock_name]
                total_earned = stock_price * share_amount

                #Add money to user funds
                user_money += total_earned

                # update user stock
                user_portfolio[stock_name]['quantity'] -= share_amount
                #update user portfolio total cost
                user_portfolio[stock_name]['total_cost'] -= total_earned

                print(f"You have sold {share_amount} of {stock_name} for {stock_price} per share.")
                print(f"Total earnings: {total_earned}")
                print(f"Your Remaining total: {user_money}")
            else:
                print("Stock not found")
        else:
            print(f"You don't have enough shares of {stock_name} to sell at this time.")
    else:
        print(f"You don't have any shares of {stock_name}")

    return user_money, user_portfolio

#Shows all the current stock data from the user
def display_stocks(stock_data):
    print("Stock Data: ")
    for stock, price in stock_data.items():
        print(f"{stock}: {price}")

def observe_portfolio():
    print("User Portfolio: ")
    for stock, data in user_portfolio.items():
        print(f"{stock}: Quantity - {data['quantity']}, Total Cost - {data['total_cost']}")

#Runs the function of loading up stock data
stock_data = load_stockdata()

#Calling function with loaded stock data
display_stocks(stock_data)

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

    #Shows stock name and price
    if user_input == 1:
       display_stocks(stock_data)
    elif user_input == 2:
        stock_name = input("What stock do you want to buy: ")
        share_amount = int(input(f"How much of {stock_name} do you want to buy: "))
        user_money, user_portfolio = buy_stock(stock_data, stock_name, share_amount, user_money, user_portfolio)
    elif user_input == 3:
        stock_name = input("What stock do you want to sell? ")
        share_amount = int(input(f"How much of {stock_name} do you want to sell? "))
        user_money, user_portfolio = sell_stock(stock_data, stock_name, share_amount, user_money, user_portfolio)
    elif user_input == 4:
        observe_portfolio()
    elif user_input == 5:
        save_portfolio(user_portfolio)
        print("Portfolio successfully saved!")
    elif user_input == 6:
        print("Thank you for checking the Stock Market today!")
        break
    else:
        print("Invalid input. Please choose a number between 1 - 6.")





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
