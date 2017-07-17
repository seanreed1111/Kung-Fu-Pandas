# Exercise 7:
# Write a program that reads an integer from the user
# Then your program should display a message indicating whether the integer is even or odd

def oddOrEven():
	num = int(raw_input("Enter a number: "))
	if (num % 2 == 0):
		print("You typed an even number")
	else:
		print("You typed an odd number")

oddOrEven()