def bottlerefund():

	smallbottles = input(("How many bottles less than or equal to one liter do you have?: "))

	largebottles = input(("How many bottles greater than one liter do you have?"))

	totalrefund = (smallbottles*0.10)+(largebottles*.25)

	totalrefund = '${:,.2f}'.format(totalrefund)

	print("The total refund is", totalrefund)

bottlerefund()
