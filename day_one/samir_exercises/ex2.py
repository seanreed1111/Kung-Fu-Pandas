# Exercise 2:
# Write a program that asks the user to enter the width and length of a room
# Once the values have been read, your program should compute and display the area of the room
# The length and the width will be entered as floating point numbers
# Include units in your prompt and output message (either feet or meters)

def areaOfRoom():
	"""Takes in width and length of a room and returns area"""
	print("Enter the length of your room (in feet)")
	length_of_room = float(raw_input("Length: "))
	width_of_room = float(raw_input("Width: "))
	area_of_room = length_of_room * width_of_room
	print("The area of your room is {}".format(area_of_room))

areaOfRoom()