#!/usr/bin/env python
# coding: utf-8

# In[1]:



import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt

a00 = np.loadtxt('data/angle_00.txt')
a010 = np.loadtxt('data/angle_010.txt')
a001 = np.loadtxt('data/angle_001.txt')
a0101 = np.loadtxt('data/angle_0101.txt')
a002 = np.loadtxt('data/angle_002.txt')
a020 = np.loadtxt('data/angle_020.txt')
a0202 = np.loadtxt('data/angle_0202.txt')

h00 = np.loadtxt('data/absh_00.txt')
h010 = np.loadtxt('data/absh_010.txt')
h001 = np.loadtxt('data/absh_001.txt')
h0101 = np.loadtxt('data/absh_0101.txt')
h002 = np.loadtxt('data/absh_002.txt')
h020 = np.loadtxt('data/absh_020.txt')
h0202 = np.loadtxt('data/absh_0202.txt')

f = np.loadtxt('data/f.txt')
f0 = np.loadtxt('data/fminmax.txt')

plt.loglog(f, a00)
plt.loglog(f, a010)
plt.loglog(f, a001)
plt.loglog(f, a0101)
plt.loglog(f, a002)
plt.loglog(f, a020)
plt.loglog(f, a0202)
plt.xlim([f0[0], f0[1]])
#plt.legend(('0,0','0.1,0','0,0.1','0.1,0.1','0,0.2','0.2,0','0.2,0.2'))
plt.savefig('figures/freqVangle.pdf')
plt.close()

plt.loglog(f, h00)
plt.loglog(f, h010)
plt.loglog(f, h001)
plt.loglog(f, h0101)
plt.loglog(f, h002)
plt.loglog(f, h020)
plt.loglog(f, h0202)
plt.xlim([f0[0], f0[1]])
#plt.legend(('0,0','0.1,0','0,0.1','0.1,0.1','0,0.2','0.2,0','0.2,0.2'))
plt.savefig('figures/freqVabsh.pdf')
plt.close()
