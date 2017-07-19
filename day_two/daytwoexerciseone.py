def is_prime(n):

	if n<=1:
		return False
	# checks each number from 2 up to but not including n to see if it divides 
	for i in range(2,n):
		if (n % i == 0):
			return False
	return True

def main():
	value = int(input("Enter an integer: "))
	if is_prime(value):
		print(value,"is prime.")
	else:
		print(value, "is not prime.")

# call the main function if the file has not been imported

if __name__ == "__main__":
	main()