import random
secret_number = random.randint(1,20)

guess = raw_input("What is the secret number?\n")
print "You guessed %s" %guess

guess = int(guess)

if guess == secret_number:
    print "You win!"
else:
    print "You lose"
