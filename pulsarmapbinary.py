import math as m
import numpy as np
import csv
import matplotlib.pyplot as plt
import pandas as pd
import astropy.coordinates as coord
from astropy.io import ascii
from astropy.coordinates import SkyCoord
import matplotlib as mpl

df = pd.read_csv('galacticwperiod.csv')

#print(plt.style.available)
xarr = np.array(df.iloc[:,0])
yarr = np.array(df.iloc[:,1])
zarr = np.array(df.iloc[:,2])

gal = SkyCoord(xarr[:], yarr[:], frame='galactic', unit='deg')


area = 100*(zarr)
mpl.style.use('seaborn-dark')
plt.figure(figsize=(6,5))
fig = plt.figure()
ax = fig.add_subplot(111, projection='aitoff')


plt.scatter(gal.l.wrap_at('180d').radian, gal.b.radian, c=zarr, cmap='gist_heat', s=area)
plt.title('Millisecond Pulsar Distribution: Galactic Coordinates', y=1.2)
plt.colorbar(label='Pulsation Period (s)') 
#cbar.set_label("Pulsation Period (s)")
#ax.set_facecolor('xkcd:battleship grey')
#fig.patch.set_facecolor('white')
ax.tick_params(axis='both', which='major', labelsize=10)
ax.grid(color='b', linestyle='solid')
plt.xlabel('Galactic Longitude', fontsize=10)
plt.ylabel('Galactic Latitude', fontsize=10)
#plt.rc('axes', size=8)
#plt.figure(figsize=(10,10))
#fig.colorbar(mesh)
plt.show()
#plt.savefig('millisecondcoloraitoff.png', dpi=600)