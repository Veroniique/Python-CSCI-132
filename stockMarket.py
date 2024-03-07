'''
7 March 2024
Objective: Stock Market simulator. Tells user to buy, sell, stocks.
           Monitors their portfolio, traces historical prices of
           a set of stocks.
TODO: - Create user prompts (7)
    - Create list to store stock prices for multiple companies
    - Use file operations to read stock data from .txt file
    - Create an output of stock name + price
    - Show history of price(s)
    - Create a quantity list to show shares owned by user and all previous purchases
    - Create functions: - transactions
                        - sufficient funds
                        - update user stock count
                        - record transaction
                        - compute networth
                        - random walk for adjusting stock prices after transaction
    - Save user data
    - Add error handling
    - Create exit message
'''

#user prompts
print("Welcome to the Stock simulator\n")
print("1. Display stocks")
print("2. Purchase stocks")
print("3. Sell stocks")
print("4. Sell stocks")
print("5. Observe portfolio")
print("6. Save portfolio")
print("7. Exit\n")
user_input = int(input("Choose a number between 1 - 7: "))

#imported libraries
import random

#Task 1.1 + 1.2 - Storing stock name + price in a list
stock_names = ["Rivian","Lego","Trek","Cisco","Crossrope","Subaru","Apple","Linux","Microsoft","Dell"]
stock_prices = ["101.5","57","120.5","350","126","400","1005","1500","1250","1000"]

#Task 1.3 - Show stock name + price
for i in range(len(stock_names)):
    print(f"The price of {stock_names[i]} stock is ${stock_prices[i]}")

#function example for creating prices
def simulate_price_change(current_price):
    '''
    Simulate a random price change for a stock.

    :param current_price:
    current_price(float): The current price of the stock.

    :return:
    float: The new price after the random walk.
    '''
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


