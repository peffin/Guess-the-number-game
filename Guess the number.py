import random

secret = random.randint(1, 50)     # pick a secret number ranges 1-99
guess = 0
tries = 0

print ("Hi, and I have a secret number for you!")
print ( "number ranges from 1 to 50.  You have 3 tries.")

# try until they guess it or run out of while loop
while guess != secret and tries < 3:
    guess = int(input("hi FEBIN, Guess a number? "))     # geting the gussed number
    if guess < secret:
        print ("Sorry Try again")
    if guess > secret:
        print ("Sorry Try again")
    tries = tries + 1                         # tries increasing by one

# printing message at the end
if guess == secret:
    print ("Congrats you win")
else:
    print ("Better luck next time")
    print ("The secret number was", secret)