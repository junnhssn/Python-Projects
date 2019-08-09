def get_level():
    res = int(input("Enter the current level of the tank : "))
    return res
    
    
def get_capacity():
    cap = int(input("Enter the capacity of the tank : "))
    return cap
    

def action(present , redmark, bluemark):
    if present > redmark :
        print("Overflow detected, Raise the alarm!!!! and close the valve. ")        
        
    elif present < bluemark :
        print("Place an order to buy more ethonal ") 
    
    else :
        print("Everything OK")
    
def main():
   
    capacity = get_capacity()
   
    high = (capacity/100)*80
   
    low = (capacity/100)*20
    
    level = get_level()
    
    action(level, high, low)
    
    
    
    
#main starts here

main()
    
    