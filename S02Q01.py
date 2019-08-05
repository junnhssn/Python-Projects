#A program to calculate the mileage of a car





def Mileage():
    distance_covered = odo_final - odo_start
    fuel_used = tank_capacity - fuel_left
    final_mileage = float(distance_covered/fuel_used)
    return final_mileage
    
#Main starts here
    
odo_start = int(input("Enter the initial reading : "))
odo_final = int(input("Enter the final reading : "))
tank_capacity = int(input("Enter the capacity of the tank : "))
fuel_left = int(input("Enter the amount of fuel left :"))


print("The mileage of the vechicle is : ",Mileage(),'Km')
