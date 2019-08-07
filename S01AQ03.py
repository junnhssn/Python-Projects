#multiplication table for any user input interger

def get_digit():
    num = int(input("enter the number : "))
    return num
   
def multi_table(number):
    
    for i in range(1,11):
         num = number*i
         print(number,'x',i,'=',num)
   
def main():
    number = get_digit()
    multi_table(number)


#main starts here
main()
