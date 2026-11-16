#This is my first python program
print  ("Hello, World!")
print ("5+3")
print (5+3)
print("store:", "Pune","| Orders today: ",18)

a = 5
b = 3
sum = a + b
print("Sum of", a, "and", b, "is:", sum)
name = input("Mukesh SINGH: ")
#float, boolean, string
c=5.0
d=True
print(type(c))
print(type(a))
print(type(5.0))
print(type(True))
print(type("Hello"))

#formatting output
print("Sum of {} and {} is {}".format(a, b, sum))
print(f"Sum of {a} and {b} is {sum}")

print(name + str(5)) # Convert the integer to a string before concatenating
#print(name +5) # This will raise a TypeError because you cannot concatenate a string and an integer directly

# Containers
# Lists, tuples, sets, dictionaries
emp_list = [] #empty list
print(type(emp_list))
emp_list = ["Mukesh", "Pune", 18, 5.0, True]
print(emp_list)




