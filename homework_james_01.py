# James Carlson
# Coding Temple - SE FT-144
# Backend Lesson 1 Assignment

# 1. Showcase Your Dance Moves! Task 1:

weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")

print()

# 1. Showcase Your Dance Moves! Task 2:
    
get_mood = input("Hello user! How do you feel today? ")

if get_mood.casefold() == "happy":
    print("That's great to hear!")
elif get_mood.casefold() == "sad":
    print("I hope your day gets better!")
else:
    print("Error! No suitable mood identified. Please try again when either happy or sad.")

print()

# 2. Python Naming Convention Practice:
# I am making an assumption that the HTML tags I'm seeing are a formatting issue and are not a part of this assignment

PI_VALUE = 3.14
user_age = 25
user_location = "New York" # this one seems correct to me; I'm assuming the user location is a variable, not a constant
MAX_LIMIT = 1000

# 3. Python Data Types and type() Function:

variable_a = "Hello, World!"    # string
variable_b = 23                 # int
variable_c = 3.14               # float
variable_d = True               # boolean

print("variable_a (\"Hello, World!\"): " + str(type(variable_a)))
print("variable_b (23):              " + str(type(variable_b)))
print("variable_c (3.14):            " + str(type(variable_c)))
print("variable_d (True):            " + str(type(variable_d))) 

print()

# 4. Arithmetic Operations in Daily Life - Task 1: Grocery Store Math

cost_eggs = 3.49
cost_potatoes = 3.59
cost_cheese = 2.69
total_grocery_cost = cost_eggs + cost_potatoes + cost_cheese
print(f"Total Grocery Cost: ${"%.2f" % total_grocery_cost}\n")

# 4. Arithmetic Operations in Daily Life - Task 2: Bank Interest

initial_amount = 6802
interest_rate = 1.06
amount_after_one_year = initial_amount  * interest_rate
print(f"Savings Account with One Year of Interest: ${"%.2f" % amount_after_one_year}\n")

# 5. Understanding Assignments and Comparisons

num1 = 13
num2 = 42
print(f"num1 = {num1}")
print(f"num2 = {num2}")

num_temp = num1
num1 = num2
num2 = num_temp
print("Behold! The numbers have been swapped!")

print(f"Evaluating: num1 ({num1}) > num2 ({num2}): {num1 > num2}")