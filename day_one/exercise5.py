'''
This program compares the sides of triangle provided by the user to determine the type of triangle
'''
def triangle():
	sides = []                                                                       #Create a list
	for i in range(3):                                                               #Convert each side provided by user to integer and append to list
		sides.append(int(input("Please enter 3 sides of a triangle: ")))

	if (sides[0] == sides[1]) & (sides[0] == sides[2]):                              #If all sides are equal indicate isolateral triangle
		print("The triangle is isolateral.")
	elif (sides[0] == sides[1]) | (sides[0] == sides[2]) | (sides[1] == sides[2]):   #If only 2 of the sides are equal we have isoscele triangle
		print("The triangle is isoscele")
	else:                                                                            #Otherwise it's a scalene triangle
		print("The trinagle is scalene")

triangle()