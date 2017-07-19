def to_roman(num):
	if((num) < 0):
		return("Number isn't a nonnegative integer.")
	elif(num == 0):
		return(" ")
	else:
		ItalianString = ""
		while(num > 0):
			if(num >= 1000):
				ItalianString += "M"
				num -= 1000
			elif(num >= 900):
				ItalianString += "CM"
				num -= 900
			elif(num >= 500):
				ItalianString += "D"
				num -= 500
			elif(num >= 400):
				ItalianString += "CD"
				num -= 400
			elif(num >= 100):
				ItalianString += "C"
				num -= 100
			elif(num >= 90):
				ItalianString += "XC"
				num -= 90
			elif(num >= 50):
				ItalianString += "L"
				num -= 50
			elif(num >= 40):
				ItalianString += "XL"
				num -= 40
			elif(num >= 10):
				ItalianString += "X"
				num -= 10
			elif(num >= 9):
				ItalianString += "IX"
				num -= 9
			elif(num >= 5):
				ItalianString += "V"
				num -= 5
			elif(num >= 4):
				ItalianString += "IV"
				num -= 4
			else:
				ItalianString += "I"
				num -= 1
		return(ItalianString)


def main():
	num = int(input("Enter a nonnegative integer: "))
	print(to_roman(num))

main()