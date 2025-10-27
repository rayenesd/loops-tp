# loops TP
# Exercise 1
# for loop
number = int()
for number in range(1,51):
    if number % 3 ==0 and number % 5 == 0 :
        print("FizzBuzz")
    elif number % 3 ==0 :
        print("Fizz")
    elif number % 5 ==0 :
        print("Buzz")
    else:
        print(number)


# Exercise 2
# while loop
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