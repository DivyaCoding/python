"""
1. Declare your age as integer variable
2. Declare your height as a float variable
3. Declare a variable that stores a complex number
4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
    Enter side a: 5
    Enter side b: 4
    Enter side c: 3
    The perimeter of the triangle is 12
Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
Calculate the slope, x-intercept and y-intercept of y = 2x -2
Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
Compare the slopes in tasks 8 and 9.
Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
Find the length of 'python' and 'dragon' and make a falsy comparison statement.
Use and operator to check if 'on' is found in both 'python' and 'dragon'
I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
There is no 'on' in both dragon and python
Find the length of the text python and convert the value to float and convert it to string
Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
Check if type of '10' is equal to type of 10
Check if int('9.8') is equal to 10
Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
    Enter number of years you have lived: 100
    You have lived for 3153600000 seconds.
Write a Python script that displays the following table
    1 1 1 1 1
    2 1 2 4 8
    3 1 3 9 27
    4 1 4 16 64
    5 1 5 25 125
"""

# 1. Declare your age as integer variable
age = 23 # declaring age variable and assigning a value to it

# 2. Declare your height as a float variable
height = 5.3 # declaring height variable and assigning a value to it

# 3. Declare a variable that stores a complex number
complex_number = 2 + 3j # declaring complex_number variable and assigning a complex number

# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input("Enter base: ")) # taking base as user input
height = float(input("Enter height: ")) # taking height as user input
area = 0.5 * base * height # calculating the area of the triangle
print("The area of the triangle is", area)

# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = float(input("Enter side a: ")) # taking side a as user input
side_b = float(input("Enter side b: ")) # taking side b as user input
side_c = float(input("Enter side c: ")) # taking side c as user input
perimeter = side_a + side_b + side_c # calculating the perimeter of the triangle
print("The perimeter of the triangle is", perimeter)

# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Enter length: ")) # taking length as user input
width = float(input("Enter width: ")) # taking width as user input
area_rectangle = length * width # calculating the area of the rectangle
perimeter_rectangle = 2 * (length + width) # calculating the perimeter of the rectangle
print("The area of the rectangle is", area_rectangle)
print("The perimeter of the rectangle is", perimeter_rectangle)

# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input("Enter radius: ")) # taking radius as user input
pi = 3.14 # assigning value of pi
area_circle = pi * radius * radius # calculating the area of the circle
circumference_circle = 2 * pi * radius # calculating the circumference of the circle
print("The area of the circle is", area_circle)
print("The circumference of the circle is", circumference_circle)

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope = 2 # the coefficient of x in the equation
y_intercept = -2 # the constant term in the equation
x_intercept = -y_intercept / slope # calculating the x-intercept
print("The slope is", slope)
print("The x-intercept is", x_intercept)
print("The y-intercept is", y_intercept)

# 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
point1 = (2, 2) # defining point 1
point2 = (6, 10) # defining point 2
slope = (point2[1] - point1[1]) / (point2[0] - point1[0]) # calculating the slope
euclidean_distance = ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5 # calculating the Euclidean distance
print("The slope is", slope)
print("The Euclidean distance is", euclidean_distance)

# 10. Compare the slopes in tasks 8 and 9.
slope_task8 = 2 # slope from task 8
slope_task9 = slope # slope from task 9
print("The slope from task 8 is", slope_task8)
print("The slope from task 9 is", slope_task9)

# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x_values = [-3, -2, -1, 0, 1, 2, 3] # defining a list of x values
for x in x_values: # iterating through the list of x values
    y = x ** 2 + 6 * x + 9 # calculating the value of y
    if y == 0: # checking if y is 0
        print("y is 0 when x =", x) # printing the x value when y is 0

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
length_python = len('python') # finding the length of 'python'
length_dragon = len('dragon') # finding the length of 'dragon'
print("The length of 'python' is", length_python) # printing the length of 'python'
print("The length of 'dragon' is", length_dragon) # printing the length of 'dragon'
print("Is the length of 'python' equal to the length of 'dragon'? ", length_python == length_dragon) # making a falsy comparison statement  

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
is_on_in_python = 'on' in 'python' # checking if 'on' is in 'python'
is_on_in_dragon = 'on' in 'dragon' # checking if 'on' is in 'dragon'
print("Is 'on' found in both 'python' and 'dragon'? ", is_on_in_python and is_on_in_dragon) # using and operator to check if 'on' is found in both 'python' and 'dragon'    

# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon." # defining the sentence
is_jargon_in_sentence = 'jargon' in sentence # checking if 'jargon' is in the sentence
print("Is 'jargon' found in the sentence? ", is_jargon_in_sentence) # printing the result   

# 15. There is no 'on' in both dragon and python
is_on_in_python = 'on' in 'python' # checking if 'on' is in 'python'
is_on_in_dragon = 'on' in 'dragon' # checking if 'on' is in 'dragon'
print("Is 'on' found in both 'python' and 'dragon'? ", is_on_in_python and is_on_in_dragon) # using and operator to check if 'on' is found in both 'python' and 'dragon'    

# 16. Find the length of the text python and convert the value to float and convert it to string
length_python = len('python') # finding the length of 'python'
length_python_float = float(length_python) # converting the length to float
length_python_str = str(length_python_float) # converting the float value to string
print("The length of 'python' as string is", length_python_str) # printing the length of 'python' as string

# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input("Enter a number: ")) # taking a number as user input
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is not even.")

# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_division = 7 // 3 # calculating the floor division of 7 by 3
int_value = int(2.7) # converting 2.7 to int    
print("Is the floor division of 7 by 3 equal to the int converted value of 2.7? ", floor_division == int_value) # making the comparison

# 19. Check if type of '10' is equal to type of 10
type_str = type('10') # getting the type of '10'
type_int = type(10) # getting the type of 10
print("Is the type of '10' equal to the type of 10? ", type_str == type_int) # making the comparison

# 20. Check if int('9.8') is equal to 10
int_value = int(float('9.8')) # converting '9.8' to float and then to int
print("Is int('9.8') equal to 10? ", int_value == 10) # making the comparison   

# 21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input("Enter hours: ")) # taking hours as user input
rate_per_hour = float(input("Enter rate per hour ")) # taking rate per hour as user input
pay = hours * rate_per_hour # calculating pay
print("Your weekly earning is:", pay) # printing the pay

# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter number of years you have lived: ")) # taking number of years as user input
seconds_in_a_year = 365 * 24 * 60 * 60 # calculating the number of seconds in a year
total_seconds = years * seconds_in_a_year # calculating the total number of seconds a person can live
print("You have lived for", total_seconds, "seconds.") # printing the total number of seconds a person can live

# 23. Write a Python script that displays the following table
print("1 1 1 1 1") # printing the first row of the table
print("2 1 2 4 8") # printing the second row of the table
print("3 1 3 9 27") # printing the third row of the table
print("4 1 4 16 64") # printing the fourth row of the table 
print("5 1 5 25 125") # printing the fifth row of the table  