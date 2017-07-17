# Exercise 3: Bottle Deposits
# In one particular jurisdiction, drink containers holding one liter or less have a $0.10 deposit
# and drink containers holding more than one liter have a $0.25 deposit.
# Write a program that reads the number of containers of each size from the user
# Your program should continue by computing and displaying the refund that will be received for returning those containers. Format the output so that it includes a dollar sign and always displays exactly two decimal places.

def bottle_deposits():
	small_bottles = float(raw_input("How many small bottles do you have? "))
	# small_bottle_total = 0.10 * small_bottles

	large_bottles = float(raw_input("How many large bottles do you have? "))

	bottle_deposit_total = small_bottles * 0.10 + large_bottles * 0.25

	print("Total Refund: ${}".format(bottle_deposit_total))

bottle_deposits()