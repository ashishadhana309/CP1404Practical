DOC = """Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%."""
sales = float(input("Enter sales: $"))
while sales >= 0:
    if 0 <= sales < 1000:
        bonus = sales * 10 / 100
        print("Bonus: $", bonus)
        sales = float(input("Enter sales: $"))
    elif sales >= 1000:
        bonus = sales * 15 / 100
        print("Bonus: $", bonus)
        sales = float(input("Enter sales: $"))
else:
    print("Invalid sales")