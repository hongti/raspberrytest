import RPi.GPIO as GPIO
import time

Btn = 21
GPIO_TRIGGER = 23
GPIO_ECHO = 24

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
    GPIO.setup(Btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(Btn, GPIO.BOTH, callback=detect, bouncetime=50)

def detect(chn):
    Print(GPIO.input(Btn))
    Distance(GPIO.input(Btn))
    
def Distance(x):
    if x == 0:
        GPIO.output(GPIO_TRIGGER, True)
    
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)
        
        start_time = time.time()
        stop_time = time.time()
        
        while GPIO.input(GPIO_ECHO) == 0:
            start_time = time.time()
            
        while GPIO.input(GPIO_ECHO) == 1:
            stop_time = time.time()
            
        time_elapsed = stop_time - start_time
        distance = (time_elapsed * 34300) / 2
        
        print("Measured distance = {:.2f} cm".format(distance))
        
def Print(x):
    if x == 0:
        print ('Measuring....')
        
def loop():
    while True:
        pass
    
if __name__ == '__main__': 
    setup()
    try:
        loop()
    except KeyboardInterrupt: 
        GPIO.cleanup()


