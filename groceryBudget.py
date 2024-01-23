'Grocery Budget Calculator'
print("Grocery Budget Calculator\n")

#User inputs about spendings
monthly_budget = int(input("What is your monthly budget for groceries?"))
item1 = float(input("What is the cost of 1 item you bought: "))
qty1 = int(input("How much did you buy of item 1: "))
item2 = float(input("What is the cost of the 2nd item you bought: "))
qty2 = int(input("How much did you buy of item 2: "))
item3 = float(input("What is the cost of 3rd item you bought: "))
qty3 = int(input("How much did you buy of item 3: "))

#calculation with the user spendings
total_cost1 = item1 * qty1
total_cost2 = item2 * qty2
total_cost3 = item3 * qty3
total_expenditure = total_cost1 + total_cost2 + total_cost3
remaining_budget = monthly_budget - total_expenditure

#outputs of the user spendings
print("\nTotal cost for first item: $" + str(total_cost1))
print("Total cost for second item: $" + str(total_cost2))
print("Total cost for third item: $" + str(total_cost3))
print("Total expenditure on groceries: $" + str(total_expenditure))
print("Remaining budget: $" + str(remaining_budget))




