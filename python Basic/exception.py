try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Invalid input value.")
    
    
    
try:
    # Open a file
    file = open('example.txt', 'r')
    # Perform some operations
except FileNotFoundError:
    print("File not found.")
finally:
    # Close the file regardless of exceptions
    file.close()



#with else conditions:
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero is not allowed.")
else:
    print("Result:", result)

