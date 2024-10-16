import sys
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def main():
    """Main REPL loop for the interactive calculator."""
    commands = {
        "add": AddCommand(),
        "subtract": SubtractCommand(),
        "multiply": MultiplyCommand(),
        "divide": DivideCommand(),
    }

    while True:
        try:
            user_input = input("Enter command (or 'exit' to quit): ")
            if user_input.lower() == "exit":
                break

            parts = user_input.split()
            command_name = parts[0]
            args = list(map(float, parts[1:]))
            
            if command_name in commands:
                result = commands[command_name].execute(*args)
                print(f"Result: {result}")
            else:
                print("Unknown command.")
        except ValueError:
            print("Invalid input. Please enter numbers.")
        except ZeroDivisionError as e:
            print(e)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
