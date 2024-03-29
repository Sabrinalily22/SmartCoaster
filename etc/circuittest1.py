from MCP3008 import MCP3008
import time, statistics
import numpy as np
import matplotlib.pyplot as plt


adc = MCP3008()

values = []
last_value = adc.read(channel = 0)
while True:
    value = adc.read(channel = 0)
    
    if last_value > 0:
        if abs((value-last_value)) < 10:
            values.append(value)        
            john = sum(values) / len(values)            

            j = len(values)
            if j>9:
                mean = sum(values[-8:])/8

                if abs(mean/john) > 0.0005:
                    means = values.append(mean)                    
                    
                else:
                    if len(means) > len(oldmeans):
                        oldmeans = means ### trigger
                    
        else: 
            values = []
    last_value = value   
    time.sleep(1) 
    
