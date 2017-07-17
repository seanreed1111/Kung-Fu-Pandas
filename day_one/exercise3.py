def deposit():
	small = int(input("Please enter the number of small conatiners " + \
		"that you want to recycle: "))
	large = int(input("Please enter the number of large conatiners " + \
		"that you want to recycle: "))

	total = small * 0.1 + large * 0.25
	total = format(round(total, 2), '.2f')

	print("Your total refund will be $" + total)

deposit()