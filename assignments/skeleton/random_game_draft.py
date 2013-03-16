import random

#Generate a random number between 1 and 20-
number = random.randint(1, 20)

print "I am thinking of a number between 1 and 20."

#Create a variable to store the number of user guesses
#At this point, the user has made 0 guesses
number_guesses = 0

while True:
    #Ask the user to guess

    #convert the number to an integer

    #update the number of gueses variable

    #Check if the guess is less than the real number
    #Let the user know if their guess is too low

    #Check if the guess is higher than the real number
    #Let the user know if their guess is too high


    #If the user gueses the right number, exit
    #the loop

#Print a message to the user showing how many guesses they've made
print "Good job! You guessed my number in %d guesses!" % (number_guesses)
