import random as rd

T = rd.randint(10,40)
H = rd.randint(30,100)

if (T > 35):
    print("Hazard Detected, Temperature\n")

if (H > 65):  
    print("Hazard Detected, Humidity\n")

print("Temperature = ",T,"°C.\n")
print("Hazard = ",H,"%.\n")
