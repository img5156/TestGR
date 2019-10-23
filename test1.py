#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys, getopt
import numpy as np
from numpy import pi
import lal
import lalsimulation as LS
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt


# In[2]:


sampling_rate=2048.
phi0 = 0.0
deltaF = 0.01
m1v = 30.0
m2v = 10.0
S1x, S1y, S1z = 0.0, 0.0, 0.99
S2x, S2y, S2z = 0.0, 0.0, 0.99
f_min = 20.0
f_ref = 20.0
f_max = sampling_rate/2.

r = 410.0 * 1.0e6 * LS.lal.PC_SI
i = 0. * pi / 180.0
lambda1, lambda2 = 0.0, 0.0

f_window_div_f_peak=1.
NumCycles=1.

waveFlags = None
amplitudeO, phaseO = 0, 7

approximant = LS.IMRPhenomHM

deltaT = 1.0 / sampling_rate
m1 = m1v * LS.lal.MSUN_SI
m2 = m2v * LS.lal.MSUN_SI


# In[3]:


nongrParams = lal.CreateDict();

hPlus, hCross = LS.SimInspiralChooseFDWaveform(m1=m1, m2=m2, 
                               S1x = S1x, S1y = S1y, S1z = S1z,
                               S2x = S2x, S2y = S2y, S2z = S2z,
                               distance = r, inclination = i, phiRef = phi0, 
                               longAscNodes=0., eccentricity=0., meanPerAno = 0.,
                               deltaF=deltaF, f_min=f_min, f_max=f_max, f_ref=f_ref,
                               LALpars=nongrParams, approximant=approximant);

f = hPlus.deltaF * np.arange(len(hPlus.data.data)) + hPlus.f0
h = hPlus.data.data + (1j)*hCross.data.data

print(hPlus.data.data, hCross.data.data)


#np.savetxt('data/f.txt',f)
#np.savetxt('data/fminmax.txt',[f_min, f_max])
np.savetxt('data/angle_0202.txt',np.unwrap(np.angle(h)))
np.savetxt('data/absh_0202.txt',np.abs(h))

exit()
iplt.figure()
#plt.loglog(f, np.unwrap(np.angle(#h)))
#plt.xlim([f_min, f_max])

plt.figure()
plt.loglog(f, np.abs(h))
plt.xlim([f_min, f_max])
