import RPi.GPIO as GPIO
import time
from tkinter import *

GPIO_TRIGGER = 23
GPIO_ECHO = 24

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
    
def detectonce():   
    print ('Measuring.... (once)')
    Distance()

def detectalways():
    print ('Measuring.... (always)')
    for i in range(5):
        Distance()
    
def Distance():
    setup()
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
    
    GPIO.cleanup()
        
    
if __name__ == '__main__':
    root = Tk()
    root.title("button shining")
    Button(root, text="测量一次", font=('KaiTi', 36, 'bold'), bg='pink', fg="green", bd=2, width=10,command = detectonce).pack()
    Button(root, text="连续测量", font=('KaiTi', 36, 'bold'), bg='pink', fg="green", bd=2, width=10,command = detectalways).pack()
    root.mainloop()
        


