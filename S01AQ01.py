def user_name():
    res = str(input("Enter your name : "))
    return res
    


def say_hello(name):
    print("Hello",name)
  

def main():
    name = user_name()  
    say_hello(name)



#main starts from here

main()
