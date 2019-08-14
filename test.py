def user_input():
    mylist = []
    
    while True:
        res = int(input('Enter a value: '))
        if res == 0:            
            break
        mylist.append(res)
        
    return [mylist,res]
    
    
    
def min_max(y):

    print("The largest number is :",max(y))
    print("The smallest number is :",min(y))


def size(x):
    counter_1 = 0
    counter_2 = 0
    counter_3 = 0

    if 0 <= x < 10 :
        counter_1 += 1 
        print("Number of single digit numbers :",counter_1)
    elif 10 <= x < 100 :
        counter_2 += 1 
        print("Number of single digit numbers :",counter_2)
    elif 100 <= x < 1000 :
        counter_3 += 1 
        print("Number of single digit numbers :",counter_3)

def main():
    numbers = user_input()
    min_max(numbers[0])
    size(numbers[1])


 
#main starts here
main()
    