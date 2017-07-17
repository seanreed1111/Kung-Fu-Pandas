def containers():
	x_dep = 0.10
	y_dep = 0.25

	x= float(input("Number of 1 litre or less than 1 litre containers: "))
	y= float(input("Number of more than 1 litre containers: "))
	Deposit= (x_dep*x)+(y_dep*y)

	print("Deposit for the Containers= ", Deposit, "$")



containers()

	