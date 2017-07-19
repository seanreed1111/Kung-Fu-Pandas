def palindrome():
	word = input(("Enter a word: "))

	wordlength = len(word)
	count = 0
	palindr = 1

	while ((count<(wordlength/2)) and (palindr == 1)):
		if word[count] != word[(wordlength - (count+1))]:
			palindr = 0;
		count+=1

	if(palindr == 1):
		print(word,"is a palindrome.")
	else:
		print(word,"isn't a palindrome.")

palindrome()
