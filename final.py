import RPi.GPIO as GPIO #module for RPi pin controls
from inputs import get_gamepad #module for gamepad controls
from time import sleep

def motor_forward(Motor1, Motor2, Motor3, Motor4, Motor5, Motor6):    
    print ("FORWARD MOTION")
#Motor1 is forward motion, Motor2 is backward motion, Motor3 turns the motor on/off    
#Here, the motor is enabled and forward motion is on high.
#The same happens with the second motor, which has inputs Motor4, 5, 6
    GPIO.output(Motor1,GPIO.HIGH)
    GPIO.output(Motor2,GPIO.LOW)
    GPIO.output(Motor3,GPIO.HIGH)
    
    GPIO.output(Motor4,GPIO.HIGH)
    GPIO.output(Motor5,GPIO.LOW)
    GPIO.output(Motor6,GPIO.HIGH)

def motor_reverse(Motor1, Motor2, Motor3, Motor4, Motor5, Motor6):
    print ("BACKWARD MOTION")
    GPIO.output(Motor1,GPIO.LOW)
    GPIO.output(Motor2,GPIO.HIGH)
    GPIO.output(Motor3,GPIO.HIGH)

    GPIO.output(Motor4,GPIO.LOW)
    GPIO.output(Motor5,GPIO.HIGH)
    GPIO.output(Motor6,GPIO.HIGH)

def motor_stop(Motor3, Motor6):
#Disables both of the motors
    GPIO.output(Motor3,GPIO.LOW)
    GPIO.output(Motor6,GPIO.LOW)

def button_input():
#Every button press returns three inputs, but only one of them is the one we need.
#This module returns a list with the input name and its state (on/off)
    events = get_gamepad()
    for event in events:
        return [event.code, event.state]

def check_move(Motor1, Motor2, Motor3, Motor4, Motor5, Motor6):
    while True:
        button = button_input()
        #BTN_TR and BTN_TL are the assigned names of the two shoulder buttons
        #which are used to control the car. All other inputs are ignored.
        if button[0] == "BTN_TR":
            if button[1] == 1:
                print("Motor start")
                motor_forward(Motor1, Motor2, Motor3, Motor4, Motor5, Motor6)
            if button[1] == 0:
                print("Motor stop")
                motor_stop(Motor3, Motor6)
        if button[0] == "BTN_TL":
            if button[1] == 1:
                print("Reverse start")
                motor_reverse(Motor1, Motor2, Motor3, Motor4, Motor5, Motor6)
            if button[1] == 0:
                motor_stop(Motor3, Motor6)
                print("Reverse stop")

def main():
    #GPIO.BOARD is the pin setup this RPi uses.
    #any warnings that occur are simply because the previously assigned
    #motors haven't been cleaned up.
    GPIO.setmode(GPIO.BOARD)
    GPIO.cleanup()
    
    Motor1 = 16    # Input Pin // yellow
    Motor2 = 18    # Input Pin // yellow
    Motor3 = 22    # Enable Pin // blue

    Motor4 = 11    # Input Pin // purple 
    Motor5 = 13    # Input Pin // purple 
    Motor6 = 15    # Enable Pin // green

#assigns the function of each of the pins. 
    GPIO.setup(Motor1,GPIO.OUT)
    GPIO.setup(Motor2,GPIO.OUT)
    GPIO.setup(Motor3,GPIO.OUT)
     
    GPIO.setup(Motor4,GPIO.OUT)
    GPIO.setup(Motor5,GPIO.OUT)
    GPIO.setup(Motor6,GPIO.OUT)
    
    check_move(Motor1, Motor2, Motor3, Motor4, Motor5, Motor6)

main()

#I know a lot of the repetitions of listing out all the 'Motors' as I did can
#be done neater with the use of classes, but hopefully this isn't too big of a
#problem.
