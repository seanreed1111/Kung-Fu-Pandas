def triangle():
	sides = []
	for i in range(3):
		sides.append(int(input("Please enter 3 sides of a triangle: ")))

	if (sides[0] == sides[1]) & (sides[0] == sides[2]):
		print("The triangle is isolateral.")
	elif (sides[0] == sides[1]) | (sides[0] == sides[2]) | (sides[1] == sides[2]):
		print("The triangle is isoscele")
	else:
		print("The trinagle is scalene")

triangle()