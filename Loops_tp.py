# loops TP
# Exercise 1
# for i in range(1,51):
#     if i :
#         print("")



# Exercise 2
secret_number = 4
guess = None
while guess != secret_number:
    guess=int(input("Please geuss the secret number: "))
    if guess<secret_number :
        print("Too Low! Try again. ")
    elif guess>secret_number :
        print("Too high! Try again. ")
    else:
        print("Congratulations! You've guessed it")
        break