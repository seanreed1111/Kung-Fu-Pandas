def table():
	print("  ",end="") 
	for i in range(1,11):
		print('{:5}'.format(i),end="")
	print()
	for m in range(1,11):
		print('{:2}'.format(m),end="")
		for n in range(1,11):
			print('{:5}'.format(n*m),end="")
		print()
table()