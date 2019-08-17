import math

def user_input():
    while True:
        res = int(input('Enter a Three digit number : '))
        if res == 0:
            break
        if 100 <= res < 1000:
            print(math.sqrt(res))
        else:
            print("Invalid input!! Please enter a positive three digit number")
user_input()
