def pattern(n):
	for  i in range(n):
		if i < n/2:
			print("*" * (i+1))
		else:
			print("*" * (n-i))

pattern(10)