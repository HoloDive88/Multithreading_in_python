import threading
import time

# Script 2: Adds Two Given Numbers and Prints the Result
def add_numbers(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is {result}")

# Script 3: Outputs Default Thread Name When Executed
def print_thread_name():
    print(f"Default thread name: {threading.current_thread().name}")

# Script 4: Timer Starts After Delay and Can Be Canceled
def start_timer(delay):
    def delayed_function():
        print("Timer has started!")

    timer = threading.Timer(delay, delayed_function)
    timer.start()

# Script 4_1: Prints Numbers from 1 to 10 with threading module
def print_numbers():
    for i in range(1, 11):
        print(i)
        time.sleep(1)

# Script 5: Creates Five Threads, Each Prints a String with a Two-Second Interval
def create_five_threads():
    def print_string(thread_name):
        print(f"{thread_name} is running")
        time.sleep(2)

    for i in range(5):
        thread = threading.Thread(target=print_string, args=(f"Thread-{i+1}",))
        thread.start()
        thread.join()

# Script 6: Takes String Input from User and Saves to a Text File
def save_input_to_file():
    user_input = input("Enter a string: ")
    with open("output.txt", "w") as file:
        file.write(user_input)
    print("Input saved to output.txt")

# Script 6_1: Runs Five Times, Takes Two Numbers, and Prints Their Sum
def repeated_sum():
    for i in range(5):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(f"The sum of {a} and {b} is {a + b}")

# Script 8: Creates a Thread, Names It, and Prints the Name
def named_thread():
    def print_thread_name():
        print(f"Thread name: {threading.current_thread().name}")

    thread = threading.Thread(target=print_thread_name, name="CustomThread")
    thread.start()
    thread.join()

# Script 9: Prints Square and Cube of a Series of Numbers
def print_square_and_cube(numbers):
    for num in numbers:
        print(f"Square of {num} is {num**2}")
        print(f"Cube of {num} is {num**3}")

# Script 11: Accesses Values of args and kwargs
def example_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# Main function to choose which script to run
def main():
    print("Choose a script to run:")
    print("2 - Add two numbers")
    print("3 - Print default thread name")
    print("4 - Start a timer")
    print("4_1 - Print numbers from 1 to 10")
    print("5 - Create five threads")
    print("6 - Save input to file")
    print("6_1 - Run repeated sum calculations")
    print("8 - Named thread")
    print("9 - Print square and cube of numbers")
    print("11 - Access args and kwargs")
    choice = input("Enter the script number: ")

    if choice == "2":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        add_numbers(a, b)
    elif choice == "3":
        print_thread_name()
    elif choice == "4":
        delay = int(input("Enter delay in seconds: "))
        start_timer(delay)
    elif choice == "4_1":
        print_numbers()
    elif choice == "5":
        create_five_threads()
    elif choice == "6":
        save_input_to_file()
    elif choice == "6_1":
        repeated_sum()
    elif choice == "8":
        named_thread()
    elif choice == "9":
        numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
        print_square_and_cube(numbers)
    elif choice == "11":
        args = (1, 2, 3)
        kwargs = {'name': "Alice", 'age': 25}
        example_function(*args, **kwargs)
    else:
        print("Invalid choice")

# Run the main function
if __name__ == "__main__":
    main()
