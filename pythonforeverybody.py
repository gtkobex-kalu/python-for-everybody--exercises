#===========================================================================================================================================================================================
#CHAPTER ONE
#================================================================================================================================================================================================================
''' 
#1 c) Store information for the long term, even beyond a power cycle.
#2 program is a sequence of instructions that can be executed by a computer.
#3 The difference between a compiler and an interpreter is that a compiler translates the entire program into machine code before execution, while an interpreter translates and executes the program line by line.
#4 a) python interpreter.
#5 It contains to problems. first problem is that primt is not difined which means print functions is misspelled. second problem is that parenthesis was expected after the function print.
#6 a) Main Memory.
#7 b) 44
#8 (1) Central processing unit in human we know that main engine is our brain so does CPU is in computers.
   (2) Main memory I don't which part of our brain stores memory but that part does as the main memory of computers store memory. 
   (3) Secondary memory we can consider this as text book which is external memory for humans. 
   (4) Input device these are similar to humans sence of organs such as eye, ear, nose and so on...
   (5) Output device and we perform output by our phisical and voice via mouth.
# The best way to avoid syntax error is trying not to make errors and you do this by running one code at a time instead of writing codes and staring at the screen to find out where is the proplem. sometimes error occurs even in very few codes so you debug the error based on the messege you have got and sharing it to others like friends or AI assistant if you can't find it. I follow this method in every day to day life.
'''
#======================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
#CHAPTER TWO
#============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
#1
from random import random


5
x = 5
x + 1
#2
name = input("What is your name: \n")
print(f"hello, {name}.")
#3
hours = input("Enter Hours: \n")
rate = input("Enter Rate: \n")
pay = float(hours) * float(rate)
print(f"Pay: {pay}")
#4
width = 17
height = 12.0
n_1 = width//2
n_2 = width/2.0
n_3 = height/3
n_4 = 1 + 2 * 5
print(n_1, type(n_1))
print(n_2, type(n_2))
print(n_3, type(n_3))
print(n_4, type(n_4))
#5
celsius = float(input("Enter temperature in Celsius: \n"))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")
#=================================================================================================================================================================================================================================================================================
#CHAPTER THREE
#==========================================================================================================================================================================================================================================================================================
#1
h = float(input('Enter hours: \n'))
r = float(input('Enter rate: \n'))
p = h * r
print(f'Hours: {h}')
print(f'Rate: {r}')
print(f'Pay: {p}')
#2
hours = input("Enter Hours: \n")
rate = input("Enter Rate: \n")
try:
    pay = float(hours) * float(rate)
    print(f"Pay: {pay}")
except ValueError:
    print("Please enter valid numbers for hours and rate.")
#3
score = input("Enter score: \n")
try:
    score = float(score)
    if score < 0.0 or score > 1.0:
        print("Error: Score must be between 0.0 and 1.0.")
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")
except ValueError:
      print("Error: Please enter a valid number for score.")
#======================================================================================================================================================================================================================
#CHAPTER FOUR
#=========================================================================================================================================================================================================================
#1
import random 
random_number = random.randint(1, 100)
print(f"Random number: {random_number}")
#2 and 3 include errors so i will not write them here.
#4 d) b and c are both correct.
#5 d) ABC Zap ABC let's try it here:
def fred():
    print("Zap")
def jane():
    print("ABC")
jane()
fred()
jane()
#6
def computepay(hours, rate):
    # Check if hours exceed standard 40 hours
    if hours > 40:
        regular_pay = 40 * rate
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        return regular_pay + overtime_pay
    else:
        return hours * rate

# Get user input outside the function
try:
    hours_input = float(input("Enter Hours: "))
    rate_input = float(input("Enter Rate: "))
    
    # Call the function with parameters
    pay = computepay(hours_input, rate_input)
    print(f"Pay: {pay}")
    
except ValueError:
    print("Error, please enter numeric input")
#7
def computegrade(score):
    if score < 0.0 or score > 1.0:
        return "Error: Score must be between 0.0 and 1.0."
    elif score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"
try:
    score_input = float(input("Enter score: "))
    grade = computegrade(score_input)
    print(f"Grade: {grade}")
except ValueError:
    print("Error: Please enter a valid number for score.")
#=============================================================================================================================================================================================================
#CHAPTER FIVE
#=============================================================================================================================================================================================================
#1
total = 0.0
count = 0

while True:
    user_input = input("Enter a number: ")
    
    # Check for exit condition first
    if user_input.lower() == 'done':
        break
        
    try:
        # Convert input to a float number
        num = float(user_input)
        total += num
        count += 1
    except ValueError:
        print("Invalid input")
        continue

# Check to avoid division by zero if 'done' is typed first
if count > 0:
    average = total / count
    print(f"{total} {count} {average}")
else:
    print("No numbers were entered.")
#2
total = 0.0
count = 0
maximum = None
minimum = None

while True:
    user_input = input("Enter a number: ")
    
    if user_input.lower() == 'done':
        break
        
    try:
        num = float(user_input)
        total += num
        count += 1
        
        # Initialize or update maximum and minimum
        if maximum is None or num > maximum:
            maximum = num
        if minimum is None or num < minimum:
            minimum = num
            
    except ValueError:
        print("Invalid input")
        continue

if count > 0:
    print(f"{total} {count} {maximum} {minimum}")
else:
    print("No numbers were entered.")
#===========================================================================================================================================================================================================================
#CHAPTER SIX
#===========================================================================================================================================================================================================================
