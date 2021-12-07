#Necessary modules
import random 
import string
import time

print('Hello there. Welcome to your random password generator\n')

#Creating a waiting timer before continuing
time.sleep(2)

def random_password_generator():
	#Length of password
	p_length = int(input('How many characters should your password be?\n'))

	#Characters from which password will be generated
	characters = list(string.ascii_letters + string.digits + "!@#$%^&*()~<>?+=-")

	#Shuffle characters into a random order
	random.shuffle(characters)

	#Set password to blank
	password = []

	#Picking random characters from list 'password length' number of times
	for i in range(p_length):
		password.append(random.choice(characters))

	#Shuffle password again
	random.shuffle(password)

	#print password to screen
	print("Your password is :  " + "".join(password))

#Call funtion to execute process
random_password_generator()

#Timer before closing program
time.sleep(10)