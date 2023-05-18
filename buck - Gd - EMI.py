# -*- coding: utf-8 -*-
from math import pi, log10, sqrt
from control import tf, bode_plot
L= 10e-6; rL=0.05; C=33e-6;rC=0.1; R=1; Vi= 10; D=0.53;
# Voltage and currents in steady state
Vo=D*Vi/(1 + rL/R); Io= Vo/R; IL=Io
# EMI Filter
Lf= 100e-6; Cf= 10e-6
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
# Plot Plant's Bode
# Note that once Hz is true, omega_limits are in Hz
mag, phase, omega = bode_plot(Gd1, dB=True, Hz=True, omega_limits=(10,200e3),\
                              omega_num=100, color="red" )
mag, phase, omega = bode_plot(Gd, dB=True, Hz=True, omega_limits=(10,200e3),\
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
i=70
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)

# EMI Filter
fs= 200e3
fc=fs/40
Cf=10e-6
Lf=1/(4*pi**2*fc**2*Cf)
print("Lf= ", Lf)









