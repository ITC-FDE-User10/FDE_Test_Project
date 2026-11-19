#name of the function, what are its inputs, and what does it return

def greet():
    """
    This function prints a greeting message.
    It does not take any inputs and does not return any value.
    """
    print("Hello! Welcome to the program.")

def run():
    """
    This function runs the main logic of the program.
    It calls the greet function and can be expanded to include more functionality.
    """
    greet()  # Call the greet function

if __name__ == "__main__":
    run()  # Execute the run function when the script is run directly
    
