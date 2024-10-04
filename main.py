import RPi.GPIO as GPIO
import time

import sensor
import motor_ctr
import PD_count

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#ports
TRIGG_PIN = 23
ECHO_PIN = 24
PHASE_PIN = 22
EN_PIN = 18

#set GPIOs
GPIO.setup(TRIGG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(PHASE_PIN, GPIO.OUT)
GPIO.setup(EN_PIN, GPIO.OUT)

#initialize motor
PWM = 0
PWM_EN = GPIO.PWM(EN_PIN, 100)
PWM_EN.start(PWM)

#set PD
kp = 2
kd = 0.5
Tp = 0.05
e = 0
e_1 = 0
yref = 0 #cm
y = 0

#misc atributes
count = 0
yref_max = 25
yref_min = 5

#get reference value
while(True):
    string = "Set y_ref from " + str(yref_min) + " to " + str(yref_max) + ": "
    odp = input(string)
    try:
        odp = int(odp)
    except:
        print("y_ref must be an int from ", yref_min, " to ", yref_max)
    else:
        if odp >= yref_min and odp <= yref_max:
            yref = odp
            break
        else:
            print("Set correct number")


#main cycle
while(1):
    y = sensor.measure(5, TRIGG_PIN, ECHO_PIN)
    e = yref - y
    
    #ending condition
    if e < 0.5 and e > -0.5:
        break
    
    u = PD_count.PD(kp, kd, Tp, e, e_1)
    motor_ctr.motor_drive(u, PHASE_PIN, PWM_EN)
    e_1 = e
    count = count + Tp

    #print signals
    if count >= 0.25:
        print("u: ", round(u))
        print("y: ", y, "\n")
        count = 0
    
    time.sleep(Tp)


PWM_EN.ChangeDutyCycle(0)
GPIO.cleanup()
