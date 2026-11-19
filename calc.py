def calculate(first: float, operator: str, second: float) -> float:
    """Return the result of a basic arithmetic operation."""
    if operator == "+":
        return first + second
    if operator == "-":
        return first - second
    if operator == "*":
        return first * second
    if operator == "/":
        return first / second
    raise ValueError("Unsupported operator. Use +, -, *, or /.")


def run() -> None:
    """Prompt for calculations until the user chooses to quit."""
    print("Calculator (+, -, *, /). Enter q as the first number to quit.")

    while True:
        try:
            first_input = input("First number: ").strip()
            if first_input.lower() == "q":
                print("Goodbye!")
                break

            first = float(first_input)
            operator = input("Operator (+, -, *, /): ").strip()
            second = float(input("Second number: ").strip())
            print(f"Result: {calculate(first, operator, second)}")
        except ValueError as error:
            print(f"Invalid input: {error}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")


if __name__ == "__main__":
    run()
