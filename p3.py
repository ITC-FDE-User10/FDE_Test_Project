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

orders = [
    {"order_id": "ORD12345", "store": "Pune", "customer_name": "Mukesh", "product": "Apple", "quantity": 3, "price": 4},
    {"order_id": "ORD12346", "store": "Mumbai", "customer_name": "Riya", "product": "Banana", "quantity": 0, "price": 2},
]

for order in orders:
    if order["quantity"] > 0:
        print(f"Order {order['order_id']} is valid")
    else:
        print(f"Order {order['order_id']} is invalid")

a = 10
b = 20
c = 30
if a > b and a > c:
    print("a is the largest")
elif b > c:
    print("b is the largest")
else:
    print("c is the largest")

if a > b or a > c:
    print("a is greater than either b or c")
else:
    print("a is not greater than either b or c")

for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
            