import RPi.GPIO as GPIO


def motor_drive(PWM, PHASE_PIN, PWM_EN):
    threshold = 5

    # signal of PWM smaller than 5 is
    # too low for motor to operate
    if PWM > threshold:
        GPIO.output(PHASE_PIN, 1)
        PWM_EN.ChangeDutyCycle(PWM)

    elif PWM < -threshold:
        GPIO.output(PHASE_PIN, 0)
        PWM_EN.ChangeDutyCycle(-PWM)

    else:
        GPIO.output(PHASE_PIN, 0)
        PWM_EN.ChangeDutyCycle(0)
