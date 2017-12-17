def my_function():
    print("Hello from my function.")

def my_function_with_args(username, greeting):
    print("Hello, %s. From my function, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

my_function()

my_function_with_args("John Doe", "a merry christmas!")

x = sum_two_numbers(1,2)
