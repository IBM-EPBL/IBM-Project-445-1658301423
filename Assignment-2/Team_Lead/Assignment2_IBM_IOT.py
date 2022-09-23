import random 

T=random.randint(18,40);
H=random.randint(20,100);

if(T>30):
    print("Hazard Detected:High Temperature","Temperature =",T,"°C");
else:
    print("No Hazard Detected:Normal Temperature","Temperature =",T,"°C");
    
if(H>90):
    print("Hazard Detected:High Humidity","Humidity =",H,"%");
else:
    print("No Hazard Detected:Normal Temperature","Humidity =",H,"%");
