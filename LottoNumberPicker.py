# Author: Michael John K. Ambait - mikeambait@outlook.com
# Description: No-frills PCSO lotto number randomizer -- without seeding
# uses python's pure 'random' module

import random

while True:
	print("########## Hello! Welcome to PCSO Lotto number picker. ##########")
	print("     Press 1 - for 6-42\n     Press 2 - for 6-45\n     Press 3 - for 6-55\n     Press Ctr+Z(Windows)/Ctrl+D(Mac/Linux) to exit")

	number = input()
	typeInt = type(1)

	#if(type(int(number)) != typeInt):
	#	print('Those that don\'t follow instructions, don\'t deserve luck\n -- Anonymous\n')
	#	break
	#make the var number int
	if(int(number) < 1):
		print('Those that don\'t follow instructions, don\'t deserve luck\n -- Anonymous\n')
		break
	elif(int(number) > 3):
		print('Those that don\'t follow instructions, don\'t deserve luck\n -- Anonymous\n')
		break 
	elif(int(number) == 1):	
		# For 6-42 
		print("Here's your lucky number:")
		for i in range(6):
			print(random.randint(1,43))
		break
	elif(int(number) == 2):
		#For 6-43
		print("Here's your lucky number:")
		for i in range(6):
			print(random.randint(1,46))
		break
	elif(int(number) == 3):
		#For 6-55
		print("Here's your lucky number:")
		for i in range(6):
			print(random.randint(1,56))
		break

	

