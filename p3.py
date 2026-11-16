#branch statements if elif else
x = 10
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

#Loop Statements
#for loop
for i in range(5):
    print(i)
       
l1 = ["Apple", "Banana", "Cherry"]
for fruit in l1:
    print(fruit)

#Comparison Operators: ==, !=, >, <, >=, <=
x = 10
y = 20
print(x == y)  # False
print(x != y)  # True
print(x > y)   # False
print(x < y)   # True
print(x >= y)  # False
print(x <= y)  # True   

order = {"order_id": "ORD12345", "store": "Pune", "customer_name": "Mukesh", "product": "Apple", "quantity": 3, "price": 4}
if order["quantity"] > 0:   
    print("Order is valid")

for order in orders:
    if order["quantity"] > 0:
        print(f"Order {order['order_id']} is valid")
    else:
        print(f"Order {order['order_id']} is invalid")
