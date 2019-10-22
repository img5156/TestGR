#!/usr/bin/env python
# coding: utf-8

# In[1]:



import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt

a00 = np.loadtxt('data/angle_00.txt')
#a010 = np.loadtxt('data/angle_010.txt')
#a001 = np.loadtxt('data/angle_001.txt')
#a0101 = np.loadtxt('data/angle_0101.txt')
#a002 = np.loadtxt('data/angle_002.txt')
#a020 = np.loadtxt('data/angle_020.txt')
a0202 = np.loadtxt('data/angle_0202.txt')

a = a00 - a0202

h00 = np.loadtxt('data/absh_00.txt')
#h010 = np.loadtxt('data/absh_010.txt')
#h001 = np.loadtxt('data/absh_001.txt')
#h0101 = np.loadtxt('data/absh_0101.txt')
#h002 = np.loadtxt('data/absh_002.txt')
#h020 = np.loadtxt('data/absh_020.txt')
h0202 = np.loadtxt('data/absh_0202.txt')

h = h00 - h0202
 
f = np.loadtxt('data/f.txt')
f0 = np.loadtxt('data/fminmax.txt')

plt.plot(f, a)
plt.xlim([f0[0], f0[1]])
#plt.legend(('0,0','0.1,0','0,0.1','0.1,0.1','0,0.2','0.2,0','0.2,0.2'))
plt.savefig('figures/diffangle.pdf')
plt.close()

plt.plot(f, h)
plt.xlim([f0[0], f0[1]])
#plt.legend(('0,0','0.1,0','0,0.1','0.1,0.1','0,0.2','0.2,0','0.2,0.2'))
plt.savefig('figures/diffabsh.pdf')
plt.close()
