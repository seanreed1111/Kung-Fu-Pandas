def fizzbuzz(m):
	for i in range(1,m):
		if i % 3 == 0 and i % 5 == 0:
			print("FizzBuzz")
		

		elif i % 5 == 0:
			print("Fizz")
		elif i % 3 == 0:
			print("Buzz")
		
		
		else:
			print(i)

fizzbuzz(100)