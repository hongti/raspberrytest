import RPi.GPIO as GPIO
import numpy as np
import time
from tkinter import *

R,G,B = 15,18,14
flag = 0

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(R, GPIO.OUT)
    GPIO.setup(G, GPIO.OUT)
    GPIO.setup(B, GPIO.OUT)
    
def detectturn():
    setup()
    Ledturn()

def detectshining():
    setup()
    Ledshining()
    
def Ledshining():
    Shining()
        
def Ledturn():
    global flag
    if flag == 0:
        GPIO.output(R, 1)
        flag = 1
    else:
        GPIO.output(R, 0)
        GPIO.output(G, 0)
        GPIO.output(B, 0)
        GPIO.cleanup()
        flag = 0

def Shining():
    t = np.random.random()
    num = (0, 1)
    for i in num:
        for j in num:
            for k in num:
                GPIO.output(R, i)
                GPIO.output(G, j)
                GPIO.output(B, k)
                time.sleep(t)
    GPIO.cleanup()
        
    
if __name__ == '__main__': 
    root = Tk()
    root.title("button shining")
    Button(root, text="led开关", font=('KaiTi', 36, 'bold'), bg='pink', fg="green", bd=2, width=10,command = detectturn).pack()
    Button(root, text="led灯闪", font=('KaiTi', 36, 'bold'), bg='pink', fg="green", bd=2, width=10,command = detectshining).pack()
    root.mainloop()


