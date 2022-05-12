import random
print("Guess a number (1 to 100)")

number = random.randint(1,100)
chances = 5
guess = 0

while chances >0:
    guess = int (input("Enter your guess:-"))
    if guess > number :
        print("Your guess was too high!")
    if guess < number :
        print("Your guess was too low!")
    chances = chances - 1
    if guess == number:
        print("You win!")
        break
    
    

if chances == 0 :
        print("You lose! The answer was",number) 
        

