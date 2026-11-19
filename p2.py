products = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Honeydew", "Indian Fig", "Jackfruit"]
print(len(products))  # length of the list
products.append("Kiwi")  # add an element to the end of the list
print(products)

#Dictionaries
products_dict = {} # empty dictionary
products_dict = {"Apple": 1.5, "Banana": 0.5, "Cherry": 2.0}
print(products_dict)

order = {"order_id": "ORD12345", 
         "store": "Pune",
         "customer_name": "Mukesh", 
         "product": "Apple", 
         "quantity": 3,
         "price": 4}
print(order)

order["quantity"] = 5  # Update the quantity
print(order)

order["price"] = 23.34
print(order)

orders = [
    {"order_id": "ORD12345", "store": "Pune", "customer_name": "Mukesh", "product": "Apple", "quantity": 3, "price": 4},
    {"order_id": "ORD12346", "store": "Mumbai", "customer_name": "Anita", "product": "Banana", "quantity": 2, "price": 1.5},
    {"order_id": "ORD12347", "store": "Delhi", "customer_name": "Ravi", "product": "Cherry", "quantity": 5, "price": 2.0}
]
print(orders[2])  # Access the third order in the list


