# Character input excercise
#name and age input
name = input("What is your name?: ")
age = input("What is your age?: ")

#Feedback to the user
year = 2018
#Formula to calculate year that they will turn 100
result = (100 - int(age))
result2 = result + int(year)

# Message addressed to them that tell them the result
print("Hello " + name + "!")
print("You will turn 100 years old in " + str(result2) + "!")