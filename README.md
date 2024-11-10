# Multithreading_in_python
Multithreading in Python is a technique that allows multiple threads to run concurrently within a single process. This can help perform tasks in parallel, making the program more efficient, especially when dealing with I/O-bound tasks such as reading/writing files, handling network requests, or waiting for user input.
This Python program showcases various beginner-friendly examples of multithreading and standard input-output tasks, organized into separate "scripts" (functions) and accessed through a main menu. Each function demonstrates a unique operation, many of which make use of the `threading` module to run tasks concurrently. Below is a description of each "script" function and what the program does as a whole.

### Overall Program Description

The program defines multiple functions, each with a specific task, such as basic arithmetic, threading examples, file handling, and more. Users can run any of these tasks by entering a choice in the main menu, which corresponds to each "script" function. The use of multithreading is demonstrated in tasks that perform concurrent execution, showing how threads can improve efficiency and responsiveness in certain operations.

### Detailed Function Descriptions

1. **`add_numbers(a, b)`**: 
   - This function takes two numbers, adds them, and prints the result.
   - Demonstrates simple arithmetic and output.

2. **`print_thread_name()`**:
   - Outputs the default name of the currently running thread.
   - Shows basic usage of `threading.current_thread()` to access thread information.

3. **`start_timer(delay)`**:
   - Creates a timer that starts executing a function (`delayed_function`) after a specified delay.
   - Demonstrates the use of `threading.Timer` for delaying function execution and using multithreading for timed tasks.

4. **`print_numbers()`**:
   - Prints numbers from 1 to 10 with a 1-second interval between each.
   - Shows how to perform a repetitive task with timed delays using `time.sleep()`.
   
5. **`create_five_threads()`**:
   - Creates five threads, each printing a message and then sleeping for 2 seconds.
   - Illustrates creating multiple threads that execute concurrently, each with a unique identifier, showcasing thread parallelism.

6. **`save_input_to_file()`**:
   - Takes a string input from the user, writes it to a text file (`output.txt`), and confirms the save.
   - Demonstrates file handling in Python and saving data to a text file.

7. **`repeated_sum()`**:
   - Runs five times, each time prompting the user to enter two numbers and printing their sum.
   - Shows repeated operations with user input in a loop.

8. **`named_thread()`**:
   - Creates a thread with a custom name (`CustomThread`) and prints this name.
   - Demonstrates creating and naming threads, showing that threads can have identifiable names.

9. **`print_square_and_cube(numbers)`**:
   - Takes a list of numbers as input and prints both the square and cube of each number.
   - Provides an example of performing calculations on multiple inputs in a batch operation.

10. **`example_function(*args, **kwargs)`**:
    - Prints both positional arguments (`args`) and keyword arguments (`kwargs`) passed to it.
    - Demonstrates Python’s capability to handle flexible argument lists in functions.

### Main Function (`main()`)

- **Menu Selection**: Displays a numbered menu with options corresponding to each of the above functions. Users can select a function by entering the respective number.
- **Input Handling**: Based on the user’s choice, the main function calls the selected function, asking for any necessary input parameters.
- **Conditional Execution**: Each choice leads to the execution of a different function, allowing users to explore multiple examples of multithreading, arithmetic, I/O operations, and function arguments.

### Example Use Cases

This program can be used to learn and practice:
- **Multithreading basics**: Shows how to create and manage threads for concurrent execution.
- **Input and output operations**: Demonstrates reading from users and writing to files.
- **Basic arithmetic and iteration**: Simple math operations and loops.
- **Function arguments**: Handles positional and keyword arguments, demonstrating flexible function definitions.

### Conclusion

This program serves as a comprehensive introduction to various programming concepts in Python, particularly focusing on multithreading. Each function demonstrates a basic yet practical operation that a beginner might encounter, making the code useful for learning and experimentation.
