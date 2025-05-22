
import random
a=random.randrange(1,100)

count=1
check=1
while check!="":
    n = input("Guess a number from 1 to 100\n")
    if a == int(n):
        print(f"Congratulations! You have guessed the number in Try # {count}\n")
    else:
        count += 1
        again = input("Your guess is wrong, Press any key to continue\n")
        if again!="":
            check="1"
        else:
            check=0
            print("The number was:",a)



