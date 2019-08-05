#multiplication table for any user input interger

def get_digit():
    num = int(input("enter the number : "))
    return num
   



def multi_table(num):
    
    
    for i in range(1,11):
         number = num*i
         print(num,'x',i,'=',number)
   



#main starts here
multi_table()
