# Exercise 4
# Exercise 4: 
# In this exercise you will create a program that reads a letter of the alphabet from the user
# If the user enters a, e, i, o or u then your program should display a message indicating that the entered letter is a vowel
# If the user enters y then your program should display a message indicating that sometimes y is a vowel, and sometimes y is a consonant
# Otherwise your program should display a message indicating that the letter is a consonant

def isVowel():
	vowels = ['a','e','i','o','u']

	user_letter = raw_input("Enter a letter: ")

	if user_letter in vowels:
		print("You entered a vowel")

	elif user_letter == "y":
		print("y is sometimes a vowel")

	else:
		print("You entered a consonant")

isVowel()