from random import randint

secret_number = randint(1 ,100)
attempts = 0

while True:
    try:
       
       guess = int(input("Guess the number(1-100):"))
       attempts +=1

       if guess == secret_number:
        print("Correct!")
        print("Attempts:" , attempts)
        break
       elif guess < secret_number:
        print("Too low!")
       else:
        print("Too high!")
    except ValueError:
        print("Invallid input! Please enter a valid number")


