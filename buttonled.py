import RPi.GPIO as GPIO

BtnPin = 21
Gpin = 23
Rpin = 24

def setup():
    GPIO.setmode(GPIO.BCM) # Numbers GPIOs by physical location
    GPIO.setup(Gpin, GPIO.OUT) # Set Green Led Pin mode to output
    GPIO.setup(Rpin, GPIO.OUT) # Set Red Led Pin mode to output
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BtnPin, GPIO.BOTH, callback=detect, bouncetime=50)
    
def Led(x):
    if x == 0:
        GPIO.output(Rpin, 1)
        GPIO.output(Gpin, 0)
    if x == 1:
        GPIO.output(Rpin, 0)
        GPIO.output(Gpin, 1)

def Print(x):
    if x == 0:
        print (' ***********************')
        print (' * Button Pressed! *')
        print (' ***********************')
            
def detect(chn):
    Led(GPIO.input(BtnPin))
    Print(GPIO.input(BtnPin))
    
def loop():
    while True:
        pass
    
def destroy():
    GPIO.output(Gpin, GPIO.HIGH) # Green led off
    GPIO.output(Rpin, GPIO.HIGH) # Red led off
    GPIO.cleanup() # Release resource
    
if __name__ == '__main__': # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt: 
        destroy()