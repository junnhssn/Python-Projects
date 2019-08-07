def get_number():
    num1 = int(input("Enter a random number : "))
    return num1
    
def perform_check(x):
    if 0 <= x < 10 :
        do_1digit_oper(x)
            
    elif  10 <= x < 100 :
        do_2digit_oper(x)
        
    elif 100 <= x < 1000 :
        do_3digit_oper(x)
        
    else :
        print("Invalid input, Please try again")
        number5 = get_number()
        perform_check(number5)
            
            
            
            
def do_1digit_oper(x):
    digit = x + 7
    unit_place = digit % 10
    print("The entered number is a single digit number :",x," and the unit place is: ", unit_place)
    
def do_2digit_oper(x):
    digit = x ** 5
    unit_place = digit % 10
    print("The entered number is a two digit number :",x," and the unit place is: ", unit_place)


def do_3digit_oper(x):
    number4 = get_number()
    digit = number4 + x
    unit_place = digit % 10
    print("The entered number is a three digit number :",x," and the unit place is: ", unit_place)






def main():
    number1 = get_number()
    
    perform_check(number1)
    
    number2 = get_number()
    
    perform_check(number2)
    
    number3 = get_number()
    
    perform_check(number3)
    
#main starts here
main()