'''
7 March 2024
Objective: Stock Market simulator. Gives user option to buy,
        sell and view stocks. Saves the user stock data to an
        external sheet called user_portfolio.txt
'''
#User money
user_money = 15000

#Function that loads up the user portfolio
def load_portfolio():
    portfolio = {}
    try:
        #Opens external sheet of user_portfolio to read data
        with open('user_portfolio.txt', 'r') as file:
            for line in file:
                stock_name, quantity, total_cost = line.strip().split(',')
                portfolio[stock_name] = {'quantity': int(quantity), 'total_cost': float(total_cost)}
    #Error checking
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
    #Open stock.txt file to read data
    with open('stock.txt', 'r') as file:
        #Read each line
        for line in file:
            #Split data in stock name and stock price
            stock_name, initial_price = line.strip().split(',')

            #Store stock data in dictionary
            stock_data[stock_name] = float(initial_price)

    return stock_data

#Function that allows user to buy stock
def buy_stock(stock_data, stock_name, share_amount, user_money, user_portfolio):
    #Check if stock exists in stock data
    if stock_name in stock_data:
        #Gets price of stock
        stock_price = stock_data[stock_name]

        #Cost calculations for buying stocks
        total_cost = stock_price * share_amount

        #Check if user has enough money
        if total_cost <= user_money:
            #Deduct money from user funds
            user_money -= total_cost
            if stock_name in user_portfolio:
                #Update user portfolio
                user_portfolio[stock_name]['quantity'] += share_amount
                user_portfolio[stock_name]['total_cost'] += total_cost
            else:
                user_portfolio[stock_name] = {'quantity': share_amount, 'total_cost': total_cost}
            #Display how much bought of stock by price and total remaining
            print(f"You have bought {share_amount} of {stock_name} for {stock_price} per share")
            print(f"Total cost: ${total_cost}")
            print(f"Your remaining total: ${user_money}")
        #Error checking
        else:
            print("You don't have enough money to buy this")
    #Error checking
    else:
        print("Stock not found in the stock data.")

    return user_money, user_portfolio

#Function that allows user to sell their stock(s)
def sell_stock(stock_data, stock_name, share_amount, user_money, user_portfolio):
    #Check if stock exists in user_portfolio
    if stock_name in user_portfolio:
        if user_portfolio[stock_name]['quantity'] >= share_amount:
            if stock_name in stock_data:
                stock_price = stock_data[stock_name]
                total_earned = stock_price * share_amount

                #Add money to user funds
                user_money += total_earned

                #Update user stock
                user_portfolio[stock_name]['quantity'] -= share_amount
                #Update user portfolio total cost
                user_portfolio[stock_name]['total_cost'] -= total_earned

                print(f"You have sold {share_amount} of {stock_name} for {stock_price} per share.")
                print(f"Total earnings: {total_earned}")
                print(f"Your Remaining total: {user_money}")
            #Error checking
            else:
                print("Stock not found")
        #Error checking
        else:
            print(f"You don't have enough shares of {stock_name} to sell at this time.")
    #Error checking
    else:
        print(f"You don't have any shares of {stock_name}")

    return user_money, user_portfolio

#Shows all the current stock data from the user
def display_stocks(stock_data):
    print("Stock Data: ")
    for stock, price in stock_data.items():
        print(f"{stock}: {price}")

#Shows the users portfolio with all their data
def observe_portfolio():
    print("User Portfolio: ")
    for stock, data in user_portfolio.items():
        print(f"{stock}: Quantity - {data['quantity']}, Total Cost - {data['total_cost']}")

#Runs the function of loading up stock data
stock_data = load_stockdata()

#Calling function with loaded stock data
display_stocks(stock_data)

#Loop that continues until a user exits the program
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
    #Asks user what stock and amount they want to buy
    elif user_input == 2:
        stock_name = input("What stock do you want to buy: ").title()
        share_amount = int(input(f"How much of {stock_name} do you want to buy: "))
        user_money, user_portfolio = buy_stock(stock_data, stock_name, share_amount, user_money, user_portfolio)
    #Asks user what stock and amount they want to sell
    elif user_input == 3:
        stock_name = input("What stock do you want to sell? ").title()
        share_amount = int(input(f"How much of {stock_name} do you want to sell? "))
        user_money, user_portfolio = sell_stock(stock_data, stock_name, share_amount, user_money, user_portfolio)
    #Shows users portfolio
    elif user_input == 4:
        observe_portfolio()
    #Saves users portfolio
    elif user_input == 5:
        save_portfolio(user_portfolio)
        print("Portfolio successfully saved!")
    #Exits the program
    elif user_input == 6:
        print("Thank you for checking the Stock Market today!")
        break
    #Error checking if user did not input a number between 1-6
    else:
        print("Invalid input. Please choose a number between 1 - 6.")