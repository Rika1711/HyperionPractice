# Compulsory Task 1
#
# Create a list called menu, which contains >=4 items in the cafe.
# Create dictionary called stock, which contains stock value of each item.
# Create dictionaty called price, which contains privces of items.
# Calculate total_stock worth in cafe - Use loop to go through dictionaries.
# Use formula item_value = (stock[items] * price[items])

menu = ['Espresso', 'Americano', 'Flat White', 'Tea', 'Carrot Cake']
stock_list  = [20,20,15,30,10]
price_list = [1,2,2.5,2,3]

stock_dict = dict(zip(menu, stock_list))
price_dict = dict(zip(menu, price_list))

item_value = []

for items in stock_dict:
    item_value.append(stock_dict[items] * price_dict[items])

total_stock = sum(item_value)

print(f"The total value of all items in my cafe is Euro {total_stock}.")

# Additional information: How much value of each item is there?

stock_value_per_item = dict(zip(menu, item_value))
print("\nDivided per item the value is as follows:")
for key, value in stock_value_per_item.items():
    print(key, ": Euro", value, )
