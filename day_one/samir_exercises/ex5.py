# Exercise 5
"""A triangle can be classified based on the lengths of its sides as equilateral, isosceles or scalene. 
All 3 sides of an equilateral triangle have the same length. 
An isosceles triangle has two sides that are the same length, and a third side that is a different length. 
If all of the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of 3 sides of a triangle from the user.
Display a message indicating the type of the triangle."""

def triangles():
	side1 = int(raw_input("Length of side 1: "))
	side2 = int(raw_input("Length of side 2: "))
	side3 = int(raw_input("Length of side 3: "))

	if side1 == side2 == side3:
		print("Equilateral")

	elif side1 == side2:
		print("Isosceles")

	elif side1 == side3:
		print("Isosceles")

	elif side2 == side3:
		print("Isosceles")

	else:
		print("Scalene")

triangles()