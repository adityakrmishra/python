# hi i am Aditya
# Today i am going to create a game 
# It is guess the number
# start it
# Let take n 
#give input to take number 
# add while loop 
# add if elif oondition
# with else funtion 
# add break condition
# print the result 
import random n =
random.randrange(1,10)
 guess = int(input("Enter any number:")) 
while n!= guess:
    if guess < n:
        print("Too low")
  guess = int(input("Enter number again:"))
    elif guess > n:
        print("Too high!")
  guess = int(input("Enter number again:"))
    else: break print("you guessed it right!!")