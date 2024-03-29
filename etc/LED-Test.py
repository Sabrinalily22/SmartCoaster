import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

red1 = 12
red2 = 16
yellow1 = 20 
yellow2 = 21
green1 = 23
green2 = 24


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


while True: 
    GPIO.output(red1, GPIO.HIGH) 
    GPIO.output(red2, GPIO.HIGH)
    GPIO.output(yellow1, GPIO.HIGH) 
    GPIO.output(yellow2, GPIO.HIGH)
    GPIO.output(green1, GPIO.HIGH) 
    GPIO.output(green2, GPIO.HIGH)
    
    time.sleep(1)

    GPIO.output(red1, GPIO.LOW) 
    GPIO.output(red2, GPIO.LOW)
    GPIO.output(yellow1, GPIO.LOW) 
    GPIO.output(yellow2, GPIO.LOW)
    GPIO.output(green1, GPIO.LOW) 
    GPIO.output(green2, GPIO.LOW)
    

    time.sleep(1)