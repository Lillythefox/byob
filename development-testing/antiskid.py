import os, sys, ctypes
#This script will detect if the stager is run in a vm or not.
#Windows only! This is basicly a pre stager.
stream = os.popen('WMIC COMPUTERSYSTEM GET MANUFACTURER')
output = stream.read()
#string cleaning 
x = output.replace("Manufacturer","")
print (x)
if x == "VMware, Inc." or x == "": #virtualbox command response needed.
    print ("stager")
    ctypes.windll.user32.MessageBoxW(0, "WARNING BYOB is running on this device this will give an atacker full control of your device if you have no idea what byob is please shutdown your computer.", "BYOB WARNING", 0)
    #rest of stager in here like normal 
else:
    sys.exit("Error: you may not use BYOB on a real computer as it is designed to be used as a learning tool.")
