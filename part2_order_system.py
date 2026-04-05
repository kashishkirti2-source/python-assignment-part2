# -------- Task 1: Explore the Menu --------

# Restaurant Menu & Order Management System
# I am using dictionaries to store menu data like category, price, and availability.
# Then I used loops to print the menu category wise.
# After that, I calculated total items, available items, most expensive item,
# and items that cost less than 150.

menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

# printing menu category wise
categories = ["Starters", "Mains", "Desserts"]

for cat in categories:
    print("\n===== " + cat + " =====")
    
    for item in menu:
        if menu[item]["category"] == cat:
            price = menu[item]["price"]
            available = menu[item]["available"]
            
            if available:
                status = "Available"
            else:
                status = "Unavailable"
            
            print(f"{item:15} ₹{price:.2f}   [{status}]")

# total number of items
total_items = len(menu)
print("\nTotal items on menu:", total_items)

# total available items
available_count = 0
for item in menu:
    if menu[item]["available"] == True:
        available_count += 1

print("Total available items:", available_count)

# most expensive item
max_price = 0
expensive_item = ""

for item in menu:
    if menu[item]["price"] > max_price:
        max_price = menu[item]["price"]
        expensive_item = item

print("Most expensive item:", expensive_item, "- ₹", max_price)

# items under 150
print("\nItems under ₹150:")
for item in menu:
    if menu[item]["price"] < 150:
        print(item, "- ₹", menu[item]["price"])


# -------- Task 2: Cart Operations --------

# In this task, I created a cart system using list of dictionaries.
# I wrote functions to add items, remove items, and update quantity.
# I also calculated the final bill including GST.

cart = []

# function to add item to cart
def add_to_cart(item_name, quantity):
    if item_name not in menu:
        print(item_name, "does not exist in menu")
        return

    if not menu[item_name]["available"]:
        print(item_name, "is currently unavailable")
        return

    # check if item already in cart
    for item in cart:
        if item["item"] == item_name:
            item["quantity"] += quantity
            print(item_name, "quantity updated to", item["quantity"])
            return

    # if item not in cart, add new entry
    cart.append({
        "item": item_name,
        "quantity": quantity,
        "price": menu[item_name]["price"]
    })
    print(item_name, "added to cart")


# function to remove item from cart
def remove_from_cart(item_name):
    for item in cart:
        if item["item"] == item_name:
            cart.remove(item)
            print(item_name, "removed from cart")
            return

    print(item_name, "not found in cart")


# function to update quantity
def update_quantity(item_name, quantity):
    for item in cart:
        if item["item"] == item_name:
            item["quantity"] = quantity
            print(item_name, "quantity updated")
            return

    print(item_name, "not found in cart")


# function to print cart
def print_cart():
    print("\nCurrent Cart:")
    for item in cart:
        print(item["item"], "- Qty:", item["quantity"])
    if len(cart) == 0:
        print("Cart is empty")


# ---- Simulation Steps ----

add_to_cart("Paneer Tikka", 2)
print_cart()

add_to_cart("Gulab Jamun", 1)
print_cart()

add_to_cart("Paneer Tikka", 1)
print_cart()

add_to_cart("Mystery Burger", 1)
print_cart()

add_to_cart("Chicken Wings", 1)
print_cart()

remove_from_cart("Gulab Jamun")
print_cart()


# -------- Order Summary --------

print("\n========== Order Summary ==========")

subtotal = 0

for item in cart:
    item_total = item["quantity"] * item["price"]
    subtotal += item_total
    print(f"{item['item']:15} x{item['quantity']}    ₹{item_total:.2f}")

print("------------------------------------")

gst = subtotal * 0.05
total = subtotal + gst

print(f"Subtotal:                ₹{subtotal:.2f}")
print(f"GST (5%):                ₹{gst:.2f}")
print(f"Total Payable:           ₹{total:.2f}")
print("====================================")


# -------- Task 3: Inventory Tracker with Deep Copy --------

# In this task, I used deep copy to create a backup of inventory.
# Then I deducted stock based on items ordered in the cart.
# I also printed reorder alerts for low stock items.

import copy

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

# making deep copy of inventory
inventory_backup = copy.deepcopy(inventory)

# change one value to show deep copy works
inventory["Paneer Tikka"]["stock"] = 5

print("\nChecking Deep Copy:")
print("Inventory:", inventory["Paneer Tikka"]["stock"])
print("Backup:", inventory_backup["Paneer Tikka"]["stock"])

# restore original inventory
inventory = copy.deepcopy(inventory_backup)


# deduct stock based on cart
print("\nUpdating Inventory after Order:")

for item in cart:
    item_name = item["item"]
    qty = item["quantity"]

    if item_name in inventory:
        available_stock = inventory[item_name]["stock"]

        if available_stock >= qty:
            inventory[item_name]["stock"] -= qty
        else:
            print("Warning:", item_name, "has only", available_stock, "units left")
            inventory[item_name]["stock"] = 0


# reorder alert
print("\nReorder Alerts:")
for item in inventory:
    stock = inventory[item]["stock"]
    reorder_level = inventory[item]["reorder_level"]

    if stock <= reorder_level:
        print(f"⚠ Reorder Alert: {item} — Only {stock} unit(s) left (reorder level: {reorder_level})")


# print inventory and backup to show difference
print("\nFinal Inventory:")
for item in inventory:
    print(item, "-", inventory[item])

print("\nBackup Inventory (Original):")
for item in inventory_backup:
    print(item, "-", inventory_backup[item])


# -------- Task 4: Daily Sales Log Analysis --------

# In this task, I analysed the sales log data.
# I calculated total revenue per day and found the best selling day.
# I also found the most ordered item.
# Then I added a new day and updated the sales report.
# Finally, I printed all orders using enumerate style numbering.


sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

# total revenue per day
print("\nRevenue Per Day:")
day_revenue = {}

for date in sales_log:
    total = 0
    for order in sales_log[date]:
        total += order["total"]
    day_revenue[date] = total
    print(date, "- ₹", total)

# best selling day
best_day = ""
max_revenue = 0

for date in day_revenue:
    if day_revenue[date] > max_revenue:
        max_revenue = day_revenue[date]
        best_day = date

print("\nBest Selling Day:", best_day, "- ₹", max_revenue)

# most ordered item
item_count = {}

for date in sales_log:
    for order in sales_log[date]:
        for item in order["items"]:
            if item in item_count:
                item_count[item] += 1
            else:
                item_count[item] = 1

most_ordered = ""
max_count = 0

for item in item_count:
    if item_count[item] > max_count:
        max_count = item_count[item]
        most_ordered = item

print("Most Ordered Item:", most_ordered, "-", max_count, "times")


# add new day
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

# reprint revenue per day
print("\nUpdated Revenue Per Day:")
day_revenue = {}

for date in sales_log:
    total = 0
    for order in sales_log[date]:
        total += order["total"]
    day_revenue[date] = total
    print(date, "- ₹", total)

# new best selling day
best_day = ""
max_revenue = 0

for date in day_revenue:
    if day_revenue[date] > max_revenue:
        max_revenue = day_revenue[date]
        best_day = date

print("\nNew Best Selling Day:", best_day, "- ₹", max_revenue)


# numbered list of all orders
print("\nAll Orders List:")
order_number = 1

for date in sales_log:
    for order in sales_log[date]:
        items = ", ".join(order["items"])
        print(f"{order_number}. [{date}] Order #{order['order_id']} — ₹{order['total']} — Items: {items}")
        order_number += 1
