# Exercise 1: 
# Write a program that asks the user to enter his or her name. 
# The program should respond with a message that says hello to the user, using his or her name

def sayHello():
	userName = raw_input("What's your name? ")
	print("Hello {}".format(userName))

sayHello()