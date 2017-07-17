'''
This program calculates the recycling deposit provided number of small and 
number of large containers
'''
def deposit():
	sDep = 0.1                                                               #Define small and large container deposit amounts
	lDep = 0.25                
	small = int(input("Please enter the number of small conatiners " + \
		"that you want to recycle: "))                                       #Convert string input to integer type
	large = int(input("Please enter the number of large conatiners " + \
		"that you want to recycle: "))

	total = small * sDep + large * lDep                                       #Calculate total deposit due 
	total = format(round(total, 2), '.2f')                                    #Round the total to the second decimal number and then format to always show 2 float points precision

	print("Your total refund will be $" + total)                              #Show screen output

deposit()