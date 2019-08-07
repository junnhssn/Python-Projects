#multiplication table for 17

def get_digit():
    num = 17
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
