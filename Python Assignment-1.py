# Q16. Write code that gives following as an output?
# iNeuroniNeuroniNeuroniNeuron

multiply_numeric_str = "iNeuron"*4
print("Multiply numeric str = ", multiply_numeric_str)

#Q17 Write a code to take number as input from the user and check if the number is odd or even?

number = int(input("Enter the number: "))

if (number%2) == 0:
    print("The given number is even")
else:
    print("The given number is odd")


# Q19 What will be the output of the following?

1 or 0
0 and 0

True and False and True

1 or 0 or 0


# Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote". 

age = int(input("Enter your age: "))

if age >= 18:
    print("I can vote")
else:
    print("I can not vote")

# Q23. Write a code that displays the sum of all the even numbers from the given list.
# numbers = [12, 75, 150, 180, 145, 525, 50]




# 24. Write a code to take 3 numbers as an input from the user and display the greatest number as output.

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
num_3 = int(input("Enter third number: "))

if num_3<num_1>num_2:
    print("The greatest number is ", num_1)
elif num_3<num_2>num_1:
    print("The greatest number is ", num_2)
else:
    print("The greatest number is ", num_3)


# Q25. Write a program to display only those numbers from a list that satisfy the following conditions

#- The number must be divisible by five

#- If the number is greater than 150, then skip it and move to the next number

#- If the number is greater than 500, then stop the loop

#numbers = [12, 75, 150, 180, 145, 525, 50]