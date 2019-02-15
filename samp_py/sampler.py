###!/usr/bin/python
#
# front matter
#
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import csv
#data = open('samp_data.smp', 'r')
#datareader = csv.reader(data, delimiter=' ')

data = np.genfromtxt('data.txt', delimiter='  ')
samp = np.genfromtxt('samp.smp', delimiter='  ', skip_header=1)
#data = np.loadtxt('data_file.txt', delimiter='  ')


pandata = pd.read_csv('data.txt')
pansamp = pd.read_csv('samp.smp')

######################################################
#sampler vectorization
time = samp[:,][:,0]
conc1 = samp[:,][:,1]
var1 = samp[:,][:,2]

avg = np.mean(time)


############################################
#export to columns
time_col = time.reshape(-1,1)
conc1_col = conc1.reshape(-1,1)
var1_col = var1.reshape(-1,1)
sdata = np.concatenate((time_col, conc1_col,var1_col), axis=1)
#save vectors
np.savetxt('samp.vec',sdata, delimiter=('  ,  '))
#Space comma space ('  ,  ') is more readable!



###########################################
# plotting
#plt.figure(1)
plt.plot(time,conc1)

#plt.figure()
plt.legend(['concentration'])
plt.xlabel('Time')
plt.ylabel('kg/m3')
plt.savefig('conc1.png')
#plt.figure(1)
plt.show()

plt.figure(2)

plt.plot(time,var1,'r-')
plt.show()
