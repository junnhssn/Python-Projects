#Program to calculate the number of stops needed for refueling



#calculation of mileage

def Mileage():
    distance_covered = odo_final - odo_start
    fuel_used = tank_capacity - fuel_left
    final_mileage = float(distance_covered/fuel_used)
    return final_mileage
#calculation of the number of stops needed  
def Stops():
    journey_distance = 560
    effective_distance = float(tank_capacity * actual_mileage)
    stops_needed = float(journey_distance/effective_distance)
    return stops_needed
    
#Main starts here
    
odo_start = int(input("Enter the initial reading : "))
odo_final = int(input("Enter the final reading : "))
tank_capacity = float(input("Enter the capacity of the tank in liters  : "))
fuel_left = int(input("Enter the amount of fuel left :"))

print("The mileage of the vechicle is : ",Mileage(),'Km')



#asking the user to enter the mileage ,we calculated in the above step

actual_mileage = float(input("Enter the calculated mileage : ")

print("The number of stops needed for refueling are : ", Stops())