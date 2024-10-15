'''
A fruit seller buys a dozen of banana at Rs.X. He sells 1 banana at Rs.Y. Write a program to determine the profit or loss in Rs. for the fruitseller.
Input format:
Input consists of 2 floating point numbers
The first input corresponds to the total cost(X)
The second input corresponds to the sold cost(Y)
Output format:
Print "Profit or Loss" with Rupees.
Sample Input:
60
4
Sample Output:
Loss : Rs.12.00
'''

def calculate_profit_loss():
    X = float(input("Enter the total cost for a dozen bananas (X): "))
    Y = float(input("Enter the selling price per banana (Y): "))
    total_selling_price = 12 * Y
    profit_loss = total_selling_price - X
    if profit_loss > 0:
        print(f"Profit : Rs.{profit_loss:.2f}")
    elif profit_loss < 0:
        print(f"Loss : Rs.{abs(profit_loss):.2f}")
    else:
        print("No Profit No Loss")
calculate_profit_loss()
