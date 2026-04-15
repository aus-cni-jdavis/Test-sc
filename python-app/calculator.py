def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    print("Simple Calculator")
    print("-----------------")

    operations = {
        "1": ("Add", add),
        "2": ("Subtract", subtract),
        "3": ("Multiply", multiply),
        "4": ("Divide", divide),
    }

    for key, (name, _) in operations.items():
        print(f"{key}. {name}")

    choice = input("\nSelect operation (1-4): ").strip()
    if choice not in operations:
        print("Invalid choice.")
        return

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number.")
        return

    name, fn = operations[choice]
    try:
        result = fn(a, b)
        print(f"\n{name}: {a} and {b} = {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
