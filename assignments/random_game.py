import random

number = random.randint(1, 20)

print "I am thinking of a number between 1 and 20."

number_guesses = 0

while True:

    guess = raw_input('Take a guess: ')

    guess = int(guess)

    number_guesses = number_guesses + 1

    if guess < number:
        print 'Your guess is too low.'

    if guess > number:
        print 'Your guess is too high.'

    if guess == number:
        break

print "Good job! You guessed my number in %d guesses!" % (number_guesses)

