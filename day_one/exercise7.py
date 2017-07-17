def integer():
	i =0 
	while i <= 0:
		i = int(input("Please enter an integer: "))
	if i%2==0:
		print(i, "is even")
	else:
		print(i, "is odd")

integer()