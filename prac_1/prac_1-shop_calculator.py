items = int(input("Number of items: "))
total = 0
while items <= 0:
    print("Invalid number")
    items = int(input("Number of items: "))
for i in range(0, items):
    price = float(input("Price of item: "))
    total += price
if total > 100:
    total = total - (total * 10 / 100)
print("Total price for", items, "items is ${:.2f}".format(total))