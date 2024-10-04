import RPi.GPIO as GPIO
import time

def measure(num_of_meas, TRIGG_PIN, ECHO_PIN):
    measurements = []
    for i in range (num_of_meas):
        GPIO.output(TRIGG_PIN, 1)
        GPIO.output(TRIGG_PIN, 0)

        loop = True
        measure_t = time.time()
        while(loop):
            if (GPIO.input(ECHO_PIN) == 1):
                start = time.time()
                loop = False
            end = time.time()
            if (end - measure_t)*1000 > 10: #ms
                loop = False

        loop = True
        while(loop):
            if (GPIO.input(ECHO_PIN) == 0):
                end = time.time()
                loop = False

        T = end - start
        T = T*1000000
        T = round(T, 0)
        d = round(T/58, 1)
        
        measurements.append(d)
    
    measurements.sort()
    d = measurements[ round((num_of_meas+1) /2 )]
    
    return d
