# this is a python comment
# this is another comment this is not really code, but it can describe what the following real code does

# print is a built-in python function that outputs a message to a screen (terminal window, UI, whatever)
print("hello from Python!")

print("another line from Python")

#variables - pices of memory that store data that can change - they can vary. that's why they're caalled variablies.
# str means string
score = 0

print("score is: " + str(score))

score = 15000

print("score is: " + str(score))

#try to change the temperature below!
temperature = 27

if (temperature < 25):
	print("maybe wear a jacket")
elif (temperature > 25):
	print("it's warm! sun's out guns out!")
else:
	print("perfect summer day")