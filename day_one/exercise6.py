'''
This function will draw triangular pattern with longest side equal to
the parameter n passed to it.
'''
def pattern(n):
	for i in range(n):
		if i < n/2:                  #While i grows up to the half of n, print i+1 times the asterix 
			print("* " * (i+1))
		else:                        #After the midpoint we reduce the number of printed asterixes by substracting i from n
			print("* " * (n-i))

pattern(9)