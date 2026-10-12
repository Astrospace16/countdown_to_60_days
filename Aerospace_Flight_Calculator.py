# Aerospace Flight Calculator 

print ("--Aerospace Flight Calculator--")

distance = float(input("Enter Flight Distance (km): "))
flight_time =  float(input("Enter Flight Duration (hr): "))

if distance > 0 and flight_time > 0:
   speed = distance / flight_time

   print (f"Flight Distance : {distance: .2f} km")
   print (f"Flight Duration : {flight_time: .2f} hr")
   print (f"Average Speed : {speed: .2f} km/hr")

else: 
   print ("Error: Distance and flight duration must be positive.")
