import numpy as np
from scipy.interpolate import interp1d

from MCP3008 import MCP3008
import time
adc = MCP3008()

# The given data points, assuming the left column is weight and the right column is voltage
#weights = np.array([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0])
#voltages = np.array([968.6744186, 962.48, 950.55, 946.27, 927.05, 899.62, 853.7807309, 605.7, 373.53, 44.05980066, 0])

weights = [1000, 900, 850, 800, 750, 700, 650, 600, 550, 500, 450, 400, 350, 300, 250, 200, 150]
voltages = [966.1, 963.708, 962.070383, 958.1441176, 942.9842105, 940.3086957, 933.5545455, 916.9166667, 894.8142857, 873.8086957, 832.4793103, 705.4225806, 441.7363636, 385.7482759, 307.7818182, 166.4457143, 55.45666667]


# using a spline interpolation
spline_model = interp1d(voltages, weights, kind='linear', fill_value="extrapolate")

# Function to predict weight from voltage using the spline model
def convert(voltage):
    return spline_model(voltage)

n = 0
""" while True:

    while n < 2**10:
        f = open("demofile2.txt", "a")
        f.write(str(predict_weight_from_voltage_spline(n)) + "\n")
        n +=1
        f.close()         

    

    voltage = adc.read(channel = 0)
    print(voltage)
    print(convert(voltage))
    time.sleep(1) """