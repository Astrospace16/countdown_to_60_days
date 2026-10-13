print ("ROCKET THRUST CALCULATOR")
print ("------------------------")

mass_flow = float(input("Enter mass flow rate (kg/s): "))
velocity = float(input("Enter exhaust velocity (m/s): "))
exit_pressure = float(input("Enter exit pressure (Pa): "))
atm_pressure = float(input("Enter atmospheric pressure (Pa): "))
exit_area = float(input("Enter exit area (m^2): "))

#Calculating thrust

momentum_thrust = mass_flow * velocity

pressure_thrust = (exit_pressure - atm_pressure) * exit_area

total_thrust = momentum_thrust + pressure_thrust

#Displaying results
print ("----------RESULTS--------------")
print (f"Momemtum Thrust: {momentum_thrust:.2f}N")
print (f"Pressure Thrust: {pressure_thrust:.2f}N")
print (f"Total Thrust: {total_thrust:.2f}N")
print (f"Thrust in kN: {total_thrust/1000:.2f}kN")