#https://tutorials-raspberrypi.com/mcp3008-read-out-analog-signals-on-the-raspberry-pi/
#https://ww1.microchip.com/downloads/aemDocuments/documents/MSLD/ProductDocuments/DataSheets/MCP3004-MCP3008-Data-Sheet-DS20001295.pdf
#https://lastminuteengineers.com/fsr-arduino-tutorial/


from MCP3008 import MCP3008
from graphing import convert
from LEDControl import *
import statistics

from datetime import datetime, timedelta
import time, csv, random
import sys


adc = MCP3008()

#test variables
time_delta = 0.5 #default every 10 minutes. 

###########

dailyWaterConsumption = 0

def calibrate(value1):    
    data = str(value1) + "\n"     
    f = open("Calibrationcurves/alpha.csv", "a")
    f.write(str(data))  
    f.close
    return
        
        

def average(input):   
    return sum(input) / len(input)

def filter(inputList):
    if len(inputList) > 10:            
        e = int(1%(0.8*len(inputList)))
        rolling = sum(inputList[-e:])/len(inputList[-e:]) 
        return(inputList)
    


def get_daily_consumption():
    print("e")    

def save_data(mass, voltage, consumption):
    currentday = current_time.strftime("%Y-%m-%d")
    currenttime = current_time.strftime("%H:%M:%S")
    data = str(currentday) + "\t" +str(currenttime) + "\t" +str(mass) + "\t" +str(voltage) + "\t" +str(consumption)+ "\n" 
    f = open("water_consumption_data", "a")
    f.write(str(data))
        
    f.close()     
    
def voltagetoweight(voltages):    
    voltage = statistics.harmonic_mean(filter(voltages))
    mass = convert(voltage) 
    return voltage, mass

last_recorded_time = datetime.now()


voltages = []
last_voltages = []
StableVoltages = []
Stablemasss = []
StableVoltage = 0
masss = 0
lastmass = 0 

while True:     
    current_time = datetime.now() 
    Voltage  =  adc.read(channel=0)  
    if Voltage > 0: 

        voltages.append(Voltage)   
        if len(voltages) == 5:
            weightDetected()

        if len(voltages) > 100: 
            StableVoltage, Stablemass = voltagetoweight(voltages)                            
            StableVoltages.append(StableVoltage)  

            if current_time - last_recorded_time > timedelta(minutes=5): 
                print(StableVoltages)
                averageStableVoltage, averageStableMass = voltagetoweight(StableVoltages)  
                print(averageStableMass)

                if lastmass > 0:
                    dailyWaterConsumption += lastmass - averageStableMass 

                save_data("%.1f" %averageStableMass, "%.1f" %averageStableVoltage, "%1f" %dailyWaterConsumption )
                log()
                lastmass = averageStableMass
                last_recorded_time = current_time  
                voltages=[]    
                StableVoltages=[]
                
                

            
        # Check if it's a new day to calculate daily consumption
        if current_time.hour == 0 and current_time.minute == 0:  # Adjust the timing as needed
            get_daily_consumption()
            dailyWaterConsumption = 0            
        
        
    else:
        if len(voltages) > len(last_voltages):
            last_voltages=voltages
        voltages=[]    
        StableVoltages=[]
        Stablemasss=[]
        last_recorded_time = current_time

    
    time.sleep(0.1)   # Adjust the sleep time as needed

"""
Read the sensor
convert to force
convert to mass (make sure this works outside of test)
read every x minutes the current mass and date/time reading and save to csv
calculate daily consumption
led = daily consumption 
todo short
calibration

"""