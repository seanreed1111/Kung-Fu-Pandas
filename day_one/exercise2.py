'''
This program calculates room area given its width and length
'''
def roomArea():
	width = float(input("Please enter the room width in meters: "))      #Convert string input to float data type
	length = float(input("Please enter the room length in meters: "))    #Convert string input to float data type

	total = width * length
	print("The area of the room is", total, "sq.m")                      #Output the area without any rounding or formatting for accuracy

roomArea()