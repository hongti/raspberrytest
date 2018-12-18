import RPi.GPIO as GPIO
import numpy as np
import time

Btn = 21
R,G,B = 15,18,14

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(R, GPIO.OUT)
    GPIO.setup(G, GPIO.OUT)
    GPIO.setup(B, GPIO.OUT)
    GPIO.setup(Btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(Btn, GPIO.BOTH, callback=detect, bouncetime=50)

def detect(chn):
    Print(GPIO.input(Btn))
    Led(GPIO.input(Btn))
    
def Led(x):
    if x == 0:
        Shining(x)      
    if x == 1:
        GPIO.output(R, 0)
        GPIO.output(G, 0)
        GPIO.output(B, 0)

def Shining(x):
    t = np.random.random()
    num = (0, 1)
    for i in num:
        for j in num:
            for k in num:
                GPIO.output(R, i)
                GPIO.output(G, j)
                GPIO.output(B, k)
                time.sleep(t)
        
def Print(x):
    if x == 0:
        print ('balabala shining!')
        
def loop():
    while True:
        pass
    
if __name__ == '__main__': 
    setup()
    try:
        loop()
    except KeyboardInterrupt: 
        GPIO.cleanup()

