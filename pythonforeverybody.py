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
