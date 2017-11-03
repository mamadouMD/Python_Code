import sys

def main():
	print"Guess a number between 1 and 100."
	randNumber = 34
	found = False    # Hold the statement of the number

	while not found:
		userGuess = input("Your guess: ")
		if userGuess == randNumber:
			print "You got it"
			found = True
		elif userGuess > randNumber:
			print "Guess lower"
		else: 
			print "Guess higher"


if __name__ == "__main__":
   main()
