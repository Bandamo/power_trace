#!/usr/bin/python

import time
import os
import numpy as np
import matplotlib.pyplot as plt

power_measured = []
t_measured = []

t = time.time()
while True:
    # Get power consumption
    f = open('/sys/class/power_supply/BAT0/power_now', 'r')
    power = float(f.read())/10**6
    f.close()

    power_measured.append(power)
    t_measured.append(time.time() - t)

    os.system('clear')
    print("Power : " + str(power) + " W")
    print("Time : " + str(time.time() - t) + " s")
    time.sleep(0.05)

    result = np.array([t_measured, power_measured])

    np.save('result.npy', result)



