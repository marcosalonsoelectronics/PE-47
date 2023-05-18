# -*- coding: utf-8 -*-
from math import pi, log10, sqrt
from control import tf, bode_plot, margin, step_response, nyquist_plot
import matplotlib.pyplot as plt
import numpy as np
L= 10e-6; rL=0.05; C=33e-6;rC=0.1; R=1; Vi= 10; D=0.53;
# Voltage and currents in steady state
Vo=D*Vi/(1 + rL/R); Io= Vo/R; IL=Io
# EMI Filter
Lf= 100e-6; Cf= 10e-6
# PWM modulator gain
kd=1
# PI compensator
R1=1.81e3; R2=1.81e3; C2=10e-9
wz=1/(R2*C2)
# Transfer functions
s = tf('s')
# Impedances definition
Zf= s*Lf/(1 + Lf*Cf*s**2)
ZL= rL + s*L
Zp= R*(1 + s*rC*C)/(1 + s*(R+rC)*C)
# Control-to-output with EMI Filter
Gd=(Vi-D*IL*Zf)*Zp/(ZL+Zp+D**2*Zf)
# Control-to-output without EMI Filter
Gd1=Vi*Zp/(ZL+Zp)
Cp=(1+s/wz)/(s/wz) # Compensator
H=1 # Sensor
# Loop gain with EMI Filter
T=Cp*kd*Gd*H
# Loop gain without EMI Filter
T1=Cp*kd*Gd1*H
# Closed-loop Control to output TF with EMI Filter
Gcl=Cp*kd*Gd/(1+T)
# Closed-loop Control to output TF without EMI Filter
Gcl1=Cp*kd*Gd1/(1+T1)
# Plot Plant's Bode
# Note that once Hz is true, omega_limits are in Hz
mag, phase, omega = bode_plot(T1, dB=True, Hz=True, omega_limits=(10,200e3),\
                              omega_num=100, color="red" )
mag, phase, omega = bode_plot(T, dB=True, Hz=True, omega_limits=(10,200e3),\
                              omega_num=100, color="blue" )    

# Print a few points
print("F(Hz)               Magnitude(dB)       Phase(deg)")
print("----------------------------------------------------------")
i=20
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=40
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=60
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=80
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)









