#Importing modules
import subprocess
import optparse

#Adjustments for the optparse module
parseobject = optparse.OptionParser()
parseobject.add_option("-i","--interface",dest="interface",help="Enter interface you want to use !")
parseobject.add_option("-m","--mac",dest="mac_address",help="New MAC address")

#Identification of inputs
(user_inputs,arguments) = parseobject.parse_args()
interface = user_inputs.interface
mac_address = user_inputs.mac_address

print("-" * 30)
print("xMacChanger Started !")
print("-" * 30)

#Changing MAC address
subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",mac_address])
subprocess.call(["ifconfig",interface,"up"])

#xMacChanger by ENES DURAN