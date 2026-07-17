expenses = []
items = []

while True:
    try:
        total_items = int(input("Enter the total number of items you bought:"))
        break
    except ValueError:
        print("Please enter a valid whole number.")

for i in range(total_items):
    while True:
        try:
            user_price = float(input("Enter amount spend:"))
            break
        except ValueError:
            print("Please enter a valid number for price.")
    
    user_item = str(input("Enter item bought:"))
    expenses.append(user_price)
    items.append(user_item)

total_amount = sum(expenses)
for i in range(total_items):
    print(f'{items[i]}: {expenses[i]}')
print(f' You spent a total of {total_amount} Rupees')
