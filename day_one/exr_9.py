def multi_table():

	for i in range(1,13):
		print(i, end="\t")
	print()
	print("______________________________________________________________________________________\n")

	for j in range(1,13):
		for k in range(1,13):
			print(j * k, end="\t")
		print("\n")

multi_table()
