# Level 1

"""
1. Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
2. Write a python comment saying 'Day 2: 30 Days of python programming'
3. Declare a first name variable and assign a value to it
4. Declare a last name variable and assign a value to it
5. Declare a full name variable and assign a value to it
6. Declare a country variable and assign a value to it
7. Declare a city variable and assign a value to it
8. Declare an age variable and assign a value to it
9. Declare a year variable and assign a value to it
10. Declare a variable is_married and assign a value to it
11. Declare a variable is_true and assign a value to it
12. Declare a variable is_light_on and assign a value to it
13. Declare multiple variable on one line
"""

'''Day 2: 30 Days of python programming''' #2. Python comment
first_name = 'Divya' #3. assigning a value to first name variable
last_name = 'B K' #4. assigning a value to last name variable
full_name = first_name + ' ' + last_name #5. assigning a value to full name variable
country = 'India' #6. assigning a value to country variable
city = 'Bangalore' #7. assigning a value to city variable
age = 23 #8. assigning a value to age variable
year = 2026 #9. assigning a value to year variable
is_married = False #10. assigning a value to is_married variable
is_true = True #11. assigning a value to is_true variable
is_light_on = True #12. assigning a value to is_light_on variable
first_name, last_name, full_name = 'Divya', 'B K', 'Divya B K' #13. declaring multiple variables on one line

# Level 2

"""
1. Check the data type of all your variables using type() built-in function
2. Using the len() built-in function, find the length of your first name
3. Compare the length of your first name and your last name
4. Declare 5 as num_one and 4 as num_two
5. Add num_one and num_two and assign the value to a variable total
6. Subtract num_two from num_one and assign the value to a variable diff
7. Multiply num_two and num_one and assign the value to a variable product
8. Divide num_one by num_two and assign the value to a variable division
9. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
10. Calculate num_one to the power of num_two and assign the value to a variable exp
11. Find floor division of num_one by num_two and assign the value to a variable floor_division
12. The radius of a circle is 30 meters.
i. Calculate the area of a circle and assign the value to a variable name of area_of_circle
ii. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
iii. Take radius as user input and calculate the area.
13. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
14. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
"""

# 1. Check the data type of all your variables using type() built-in function
print(type(first_name)) # checking the data type of first name variable
print(type(last_name)) # checking the data type of last name variable
print(type(full_name)) # checking the data type of full name variable
print(type(country)) # checking the data type of country variable
print(type(city)) # checking the data type of city variable
print(type(age)) # checking the data type of age variable
print(type(year)) # checking the data type of year variable
print(type(is_married)) # checking the data type of is_married variable
print(type(is_true)) # checking the data type of is_true variable
print(type(is_light_on)) # checking the data type of is_light_on variable

# 2. Using the len() built-in function, find the length of your first name
print(len(first_name)) # finding the length of first name variable

# 3. Compare the length of your first name and your last name
print(len(first_name) == len(last_name)) # comparing the length of first name and last name

# 4. Declare 5 as num_one and 4 as num_two
num_one = 5 # declaring num_one variable and assigning a value to it
num_two = 4 # declaring num_two variable and assigning a value to it

# 5. Add num_one and num_two and assign the value to a variable total
total = num_one + num_two # adding num_one and num_two and assigning the value to total variable

# 6. Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two # subtracting num_two from num_one and assigning the value

# 7. Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two # multiplying num_one and num_two and assigning the value to product variable

# 8. Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two # dividing num_one by num_two and assigning the value to division variable

# 9. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_one % num_two # finding the remainder of num_one divided by num_two and assigning the value to remainder variable

# 10. Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two # calculating num_one to the power of num_two and assigning the value to exp variable

# 11. Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two # finding the floor division of num_one by num_two and assigning the value to floor_division variable

''' 
12. The radius of a circle is 30 meters.
i. Calculate the area of a circle and assign the value to a variable name of area_of_circle
ii. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
iii. Take radius as user input and calculate the area.
'''
radius = 30 # declaring radius variable and assigning a value to it
area_of_circle = 3.14 * radius ** 2 # calculating the area of a circle and assigning the value to area_of_circle variable
circum_of_circle = 2 * 3.14 * radius # calculating the circumference of a circle and assigning the value to circum_of_circle variable
radius_input = float(input("Enter the radius of the circle: ")) # taking radius as user input
area_of_circle_input = 3.14 * radius_input ** 2 # calculating the area of a circle using user input and assigning the value to area_of_circle_input variable
print("Area of the circle with radius", radius_input, "is:", area_of_circle_input) # printing the area of the circle using user input

# 13. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name_input = input("Enter your first name: ") # taking first name as user input
last_name_input = input("Enter your last name: ") # taking last name as user input
country_input = input("Enter your country: ") # taking country as user input
age_input = int(input("Enter your age: ")) # taking age as user input

# 14. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')