def anagram(string1, string2):
	if len(string1) != len(string2):
		print("Nice Try Buddy")
		return
	else:
		dict1 = {}
		dict2 = {}
		for character in string1:
			if character in dict1.keys():
				dict1[character] += 1
			else:
				dict1[character] = 1
		print(dict1)
		for character1 in string2:
			if character1 in dict2.keys():
				dict2[character1] += 1
			else:
				dict2[character1] = 1
		print(dict2)
		if dict1 == dict2:
			print("Hooray, {} is an anagram of {}".format(string1, string2))
		else:
			print("Nice Try Buddy")

def main():
	string1 = input("Enter a word: ")
	string2 = input("Enter a second word: ")

	anagram(string1, string2)

if __name__ == "__main__":
	main()