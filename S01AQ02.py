#multiplication table for any user input interger


def multi_table():
    num = int(input("enter the number : "))
    
    for i in range(1,11):
         number = num*i
         print(num,'x',i,'=',number)
   



#main starts here
multi_table()
