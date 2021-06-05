def choose_number():
    print("Choose a number from range 1-1000 and I will guess it in 10 trials.")

choose_number()

# def guess_number(min, max):
#     guess = int((max - min)/2 + min)
#     print("My guess is: ")
#     return guess
#
# print(guess_number(0,1000))

def check_guess():
    min = 0
    max = 1000
    guess = int((max - min) / 2 + min)
    print("My guess is: " + str(guess))

    for i in range(10):
        response = input("choose: 1 = too small, 2 = too big, 3 = I win: ")
        if response == "3":
            return "I win"

        elif response == "2":
            max = guess
            guess = int((max - min) / 2 + min)
            print(guess)
            continue

        elif response == "1":
            min = guess
            guess = int((max - min) / 2 + min)
            print(guess)
            continue

        else:
            return "Wrong data provided"


print(check_guess())