def multtbl():
	for i in range(0,11,1):
		if(i == 0):
			print("   ", end="")
		else:
			print ("{:4}".format(i), end=" ")
	print(" ")
	for j in range(1,11,1):
		print("{:2}".format(j), end=" ")
		for k in range(1,11,1):
			print ("{:4}".format(j*k), end=" ")
		print(" ")


multtbl()