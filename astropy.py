#import numpy to work with numbers and lists of numbers easily.
import numpy as np

#import pyplot from matplotlib to help us draw graphs and pictures
import matplotlib.pyplot as plt

#import fits from astropy.io to open and use special space picture files called FITS
from astropy.io import fits

#Import download_file from astropy.utils.data to grab data from the internet without leaving our code.
from astropy.utils.data import download_file

#import Logstreach and powerstrech from astropy.visualization to make our space pictures look clearer/
from astropy.visualization import LogStretch, PowerStretch

#import ImageNormalize from astropy.visualization to help make sure our pictures show up nicely in our graphs
from astropy.visualization.mpl_normalize import ImageNormalize

#use this function to download a space image stored in a FITS file
image_file2 = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True)
#image_file = download_file('https://chandra.harvard.edu/photo/2014/igrj11014/fits/igrj11014-6103_broad_smooth.fits', cache=True)

image_data2 = fits.getdata(image_file2)
import pprint #pretty print moduel
header2 = fits.getheader(image_file2)
pprint.pprint(header2)

print('Min:', np.min(image_data2))
print('Max:', np.max(image_data2))
print('Mean:', np.mean(image_data2))
print('Stdev:', np.std(image_data2))

plt.figure(figsize=(10,10)) #set the size of the image
plt.imshow(image_data2, cmap='cividis')
plt.colorbar()
plt.show()
