def roomArea():
	width = float(input("Please enter the room width in meters: "))
	length = float(input("Please enter the room length in meters: "))

	total = width * length
	print("The area of the room is", total, "sq.m")

roomArea()