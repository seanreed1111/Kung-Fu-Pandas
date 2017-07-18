def triangle_name():
	x = (input("x: "))
	y = (input("y: "))
	z = (input("z: "))

	if x == y == z:
		print("It is an equilateral triangle")
	elif x != y != z:
		print("It is a scalene triangle")
	else:
		print("It is an isosceles triangle")

triangle_name()

