from MCP3008 import MCP3008
import time
import csv
import numpy as np
import matplotlib.pyplot as plt


adc = MCP3008()

n = 1
m = True
while m == True:
    value = adc.read(channel = 0)
    
    print(adc.read(channel = 0))

    with open('Calibrationcurves/600.csv', mode='a', newline='\n' ) as file:
        writer = csv.writer(file)
        stri = str(value)        
        writer.writerow(str(value))
    
    print(n)
    n += 1
    time.sleep(1) 
    if n == 1200:
        m = False   
    