from MCP3008 import MCP3008
import time



adc = MCP3008()
x = True
n = 0
i = 0
while x == True:
 
    value = adc.read(channel = 0)
    
    time.sleep(0.10)
    n += value
    i += 1
    if i == 50:
        x = False
value = n/i
print("final " +str(value))

fsrVoltage = value / 1023.0 * 5
print(fsrVoltage)

 #The voltage = Vcc * R / (R + FSR) where R = 10K and Vcc = 5V
#so FSR = ((Vcc - V) * R) / V        yay math!
fsrResistance = 5.2 - fsrVoltage 
fsrResistance *= 10000
fsrResistance /= fsrVoltage
print("FSR Resistance in ohms = " +str(fsrResistance))


fsrConductance = 1000000;           
fsrConductance /= fsrResistance

value1 = (fsrResistance + 30)/(245/249)
value2 = (value1*0.00412 -13.558)


print(value1)
print(fsrResistance/value2)

""""
if (fsrConductance <= 1000):
    fsrForce = fsrConductance / 80
    print("Force in Newtons: ")
    print(fsrForce)
    print(fsrForce *9.81*10*2.4)     
else:
    fsrForce = fsrConductance - 1000
    fsrForce /= 30
    print("Force in Newtons: ")
    print(fsrForce)
    print(fsrForce*9.81*10*2.45);            
"""