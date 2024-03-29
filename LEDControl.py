import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#assign GPIO position
red1 = 12
red2 = 16
yellow1 = 20 
yellow2 = 21
green1 = 23
green2 = 24

#set LEDS doutput and start low
GPIO.setup(red1, GPIO.OUT)
GPIO.output(red1, GPIO.LOW)
GPIO.setup(red2, GPIO.OUT)
GPIO.output(red2, GPIO.LOW)

GPIO.setup(yellow1, GPIO.OUT)
GPIO.output(yellow1, GPIO.LOW)
GPIO.setup(yellow2, GPIO.OUT)
GPIO.output(yellow2, GPIO.LOW)

GPIO.setup(green1, GPIO.OUT)
GPIO.output(green1, GPIO.LOW)
GPIO.setup(green2, GPIO.OUT)
GPIO.output(green2, GPIO.LOW)

#Flash on/off twice
def all_flash():
    GPIO.output(red1, GPIO.HIGH) 
    GPIO.output(red2, GPIO.HIGH)
    GPIO.output(yellow1, GPIO.HIGH) 
    GPIO.output(yellow2, GPIO.HIGH)
    GPIO.output(green1, GPIO.HIGH) 
    GPIO.output(green2, GPIO.HIGH)
    
    time.sleep(0.5)

    GPIO.output(red1, GPIO.LOW) 
    GPIO.output(red2, GPIO.LOW)
    GPIO.output(yellow1, GPIO.LOW) 
    GPIO.output(yellow2, GPIO.LOW)
    GPIO.output(green1, GPIO.LOW) 
    GPIO.output(green2, GPIO.LOW)
    
    time.sleep(0.5)

    GPIO.output(red1, GPIO.HIGH) 
    GPIO.output(red2, GPIO.HIGH)
    GPIO.output(yellow1, GPIO.HIGH) 
    GPIO.output(yellow2, GPIO.HIGH)
    GPIO.output(green1, GPIO.HIGH) 
    GPIO.output(green2, GPIO.HIGH)

    time.sleep(0.5)

    GPIO.output(red1, GPIO.LOW) 
    GPIO.output(red2, GPIO.LOW)
    GPIO.output(yellow1, GPIO.LOW) 
    GPIO.output(yellow2, GPIO.LOW)
    GPIO.output(green1, GPIO.LOW) 
    GPIO.output(green2, GPIO.LOW)

def weightDetected():
   
    GPIO.output(yellow1, GPIO.HIGH) 
    GPIO.output(yellow2, GPIO.HIGH)
    
    
    time.sleep(0.5)

    
    GPIO.output(yellow1, GPIO.LOW) 
    GPIO.output(yellow2, GPIO.LOW)
   
    
    time.sleep(0.5)

    GPIO.output(yellow1, GPIO.HIGH) 
    GPIO.output(yellow2, GPIO.HIGH)


    time.sleep(0.5)

    GPIO.output(yellow1, GPIO.LOW) 
    GPIO.output(yellow2, GPIO.LOW)

def log():
    GPIO.output(yellow1, GPIO.HIGH) 
    time.sleep(0.1)
    GPIO.output(yellow1, GPIO.LOW)  
    time.sleep(0.2)
    GPIO.output(yellow1, GPIO.LOW)   
    GPIO.output(yellow1, GPIO.HIGH) 
    time.sleep(0.1)
    GPIO.output(yellow1, GPIO.LOW) 
    

def weightPercentile(percent):
    if percent > 0:
        GPIO.output(red1, GPIO.LOW) 
        GPIO.output(red2, GPIO.LOW)
        GPIO.output(yellow1, GPIO.LOW) 
        GPIO.output(yellow2, GPIO.LOW)
        GPIO.output(green1, GPIO.LOW) 
        GPIO.output(green2, GPIO.LOW)
    elif percent > 1/6:
        GPIO.output(red1, GPIO.HIGH) 
    elif percent > 2/6: 
        GPIO.output(red1, GPIO.HIGH) 
        GPIO.output(red2, GPIO.HIGH)   
    elif percent > 3/6:
        GPIO.output(red1, GPIO.HIGH) 
        GPIO.output(red2, GPIO.HIGH)
        GPIO.output(yellow1, GPIO.HIGH) 
    elif percent > 4/6:
        GPIO.output(red1, GPIO.HIGH) 
        GPIO.output(red2, GPIO.HIGH)
        GPIO.output(yellow1, GPIO.HIGH) 
        GPIO.output(yellow2, GPIO.HIGH)
    elif percent > 5/6:
        GPIO.output(red1, GPIO.HIGH) 
        GPIO.output(red2, GPIO.HIGH)
        GPIO.output(yellow1, GPIO.HIGH) 
        GPIO.output(yellow2, GPIO.HIGH)
        GPIO.output(green1, GPIO.HIGH) 
    elif percent > 6/6:
        GPIO.output(red1, GPIO.HIGH) 
        GPIO.output(red2, GPIO.HIGH)
        GPIO.output(yellow1, GPIO.HIGH) 
        GPIO.output(yellow2, GPIO.HIGH)
        GPIO.output(green1, GPIO.HIGH) 
        GPIO.output(green2, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(red1, GPIO.LOW) 
    GPIO.output(red2, GPIO.LOW)
    GPIO.output(yellow1, GPIO.LOW) 
    GPIO.output(yellow2, GPIO.LOW)
    GPIO.output(green1, GPIO.LOW) 
    GPIO.output(green2, GPIO.LOW)