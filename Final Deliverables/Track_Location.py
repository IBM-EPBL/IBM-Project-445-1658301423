import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
import requests
import json

#Provide your IBM Watson Device Credentials
organization = "90mku9"
deviceType = "GPS"        #Credentials of Watson IoT sensor simulator
deviceId = "1923"
authMethod = "token"
authToken = "d3i!ptnd7K9D*lqm+w"


# Initialize the device client.
L=0

try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()
while True:
    i = random.uniform(13.08017,28.69365)
    la =round(i,6)
    m=random.uniform(72.86676,80.23717)
    lo =round(m,6)
    #Send random data to node-red to IBM Watson
    data = { 'Latitude' : la, 'Longitude' : lo}
    print(data)
    def myOnPublishCallback():
        print("\nPublished gprs location = to IBM Watson\n")

    success = deviceCli.publishEvent("Data", "json", data, qos=0, on_publish=myOnPublishCallback)
    time.sleep(60)
    if not success:
        print("Not connected to IoTF")
    time.sleep(1)
    
deviceCli.disconnect()
