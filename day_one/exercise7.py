'''
This function takes integer input from user and determines if it is even or odd
'''
def integer():
	i = 0                                             #Set up a centinel value for basic user input validation
	while i <= 0:                                     #Until input is not positive integer, flow control will keep asking for integer input
		i = int(input("Please enter an integer: "))
	if i%2==0:                                        #If number divides by 2 without remainder then we have an even number
		print(i, "is even")
	else:                                             #Otherwise it must be odd
		print(i, "is odd")

integer()