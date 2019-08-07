#Program to check whether the entered number is two digit or a three digit number.


def get_number():
    num1 = int(input("Enter a random number : "))
    return num1
    
def perform_check(x):

        if 10 <= x < 100 :
            print("The given number",x,"is a two digit number")
        
        elif 100 <= x < 1000 :
            print("The given number",x,"is a three digit number")
        
        else :
            print("The entered number is: ", x,)
        
        
def main():
    number1 = get_number()
    number2 = get_number()
    perform_check(number1)
    perform_check(number2)
   
    
# main start here
main()
        