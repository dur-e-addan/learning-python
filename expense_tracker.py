expenses = []
items = []
total_items = int(input("Enter the total number of items you bought:"))
for i in range(total_items):
    user_price = int(input("Enter amount spend:"))
    user_item = str(input("Enter item bought:"))
    expenses.append(user_price)
    items.append(user_item)
total_amount = sum(expenses)
for i in range(total_items):
    print(f'{items[i]}: Rs.{expenses[i]}')
print(f' You spent a total of {total_amount} Rupees.')
