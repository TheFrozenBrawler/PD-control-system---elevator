
def PD(kp, kd, Tp, e, e_1):

    u = e*kp + kd*(e-e_1)/Tp
    
    # change signal in case where it's to small to 
    # move the platform (voltage to low)

    if u > 0 and u < 40:
        u = 40
    
    elif u < 0 and u > -15:
        u = -15
    
    elif u > 100:
        u = 100

    elif u < -100:
        u = -100

    ''' unchanged value if signal
        is between -100 and -15,
        40 and 100 '''

    return u
