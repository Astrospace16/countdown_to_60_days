print ("AIRCRAFT PERFORMANCE CALCULATOR")

velocity = float(input("Enter velocity (m/s): "))
air_density = float(input("Enter air density (kg/m^3): "))
wing_area = float(input("Enter wing area (m^2): "))
lift_coefficient = float(input("Enter lift coefficient (Cl): "))
drag_coefficient = float(input("Enter drag coefficient (Cd): "))

#Calculating lift and drag

if velocity <= 0 or air_density <= 0 or wing_area <= 0:
    print("Error: Velocity, air density, and wing area must be greater than zero.")

elif lift_coefficient <= 0 or drag_coefficient <= 0:
    print("Error: Lift and drag coefficients must be greater than zero.")

else: 

    dynamic_pressure = 0.5 * air_density * velocity**2

    lift = 0.5 * air_density * velocity**2 * wing_area * lift_coefficient
    drag = 0.5 * air_density * velocity**2 * wing_area * drag_coefficient

    #Displaying results
    print ("----------RESULTS--------------")
    print (f"Lift: {lift:.2f}N")
    print (f"Drag: {drag:.2f}N")        

    print (f"Dynamic Pressure: {dynamic_pressure:.2f}Pa")