"""
Script for generating map for the CTD deployments from in2020_e01 (she384, Sept. 2020)

Plots the locations of CTD deployments that took place on in2020_e01 that were relevant to the commissioning
of two new dissolved oxygen instruments

"""

""" Imports """
# Import cartopy map plotting library + utilities
import cartopy.crs as ccrs
from cartopy.io import shapereader
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

import matplotlib.pyplot as plt
import matplotlib as mpl

import pandas as pd
import numpy as np
from netCDF4 import Dataset
from datetime import datetime

# Import PIL to make image buffer heaps bigger for HQ plots. Not necessary for SVG output though.
from PIL import Image
Image.MAX_IMAGE_PIXELS = 233280000

# Just for profiling the script runtime
start_time = datetime.now()

# Set some Matplotlib chart styling of the plot
mpl.rc('font', family='serif')
mpl.rc('figure', figsize=(6, 6))

# Import data files. The .shp is used for plotting a super HQ coastline of Australia+Tasmania that I made personally.
df = pd.read_csv(r"C:\Users\she384\Documents\DO Commissioning\repo\data\ctd_deployment_locations.csv")
shp = shapereader.Reader(r"C:\Users\she384\Documents\High-res-aus\highres_aus.shp")

""" Set map extents """
extent = [146, 149, -42, -44.50]

x_locs = np.linspace(146, 149, 5)
y_locs = np.linspace(-42, -44.5, 5)

# Function to handle creating all of the map things from Cartopy
def make_map(projection=ccrs.PlateCarree()):
    fig, ax = plt.subplots(figsize=(15, 8), subplot_kw=dict(projection=projection))
    grid_lines = ax.gridlines(draw_labels=True, alpha=0.3, color='black',

                              xlocs=x_locs,
                              ylocs=y_locs)
    grid_lines.xlabels_top = grid_lines.ylabels_right = False
    grid_lines.xformatter = LONGITUDE_FORMATTER
    grid_lines.yformatter = LATITUDE_FORMATTER
    grid_lines.xlabel_style = {'size': 14}
    grid_lines.ylabel_style = {'size': 14}

    return fig, ax


fig, ax = make_map(projection=ccrs.PlateCarree())
ax.set_extent(extent)

""" 
This section of code pertains to the plotting of bathymetry lines from the highest quality GEBCO 
product. The NetCDF file is approximately 1.8gb in full, so plotting the whole thing would take years,
in this code it gets cut down to match the plotting extents (lat_bounds and lon_bounds)

GEBCO bathymetry datafiles can be found at: www.gebco.net
Find the file used in this script here: https://www.bodc.ac.uk/data/open_download/gebco/GEBCO_30SEC/zip/

"""
mapdata = Dataset('C:/Users/she384/Downloads/GEBCO_2014/GEBCO_2014_2D.nc')

lat_bounds = [-45, -40]
lon_bounds = [146, 149]

map_lat = mapdata.variables['lat'][:]
map_lon = mapdata.variables['lon'][:]

lat_low_ind = np.argmin(np.abs(map_lat - lat_bounds[0]))
lat_upp_ind = np.argmin(np.abs(map_lat - lat_bounds[1]))
to_plot_lat = mapdata.variables['lat'][lat_low_ind:lat_upp_ind]

lon_low_ind = np.argmin(np.abs(map_lon - lon_bounds[0]))
lon_upp_ind = np.argmin(np.abs(map_lon - lon_bounds[1]))
to_plot_lon = mapdata.variables['lon'][lon_low_ind:lon_upp_ind]

height = mapdata.variables['elevation'][lat_low_ind:lat_upp_ind, lon_low_ind:lon_upp_ind]

mainmap = ax.contour(to_plot_lon, to_plot_lat, height, vmax=5000, transform=ccrs.PlateCarree(), cmap='bone',
                    linewidths=0.5, levels=[-6000, -5000, -4000, -3000, -2000, -1000, -500], alpha=0.4)
# Label the isobars with a dictionary so it is pretty
fmt_dictionary = {-6000: '6000m', -5000: '5000m', -4000: '4000m', -3000: '3000m', -2000: '2000m', -1000: '1000m',
                  -500: '500m'}
ax.clabel(mainmap, [-6000, -5000, -4000, -3000, -2000, -1000, -500], fmt=fmt_dictionary)

"""   End of GEBCO bathymetry plotting   """

# You can add a ocean feature from Cartopy, but a cheating way is to just set the figure background color to
# match the ocean...
ax.background_patch.set_facecolor('#bde1f1')

# Plot on the HQ shape file coastline
for record, geometry in zip(shp.records(), shp.geometries()):
    ax.add_geometries([geometry], ccrs.PlateCarree(), facecolor='#c4c8ce', edgecolor='black', lw=0.5)

# Plot the CTD deployment locations along with a little custom annotation offset otherwise they overlap
for row in df.iterrows():
    row = row[1]
    plt.plot(row['Longitude'], row['Latitude'], marker="o", lw=0, mfc='#f2f542', mec='#dbd814', ms=14, zorder=20)
    if row['Deployment'] == 1:
        offset = 0.02
    else:
        offset = -0.04
    plt.annotate(f"Dep. {row['Deployment']}", (row['Longitude']+0.05, row['Latitude']+offset), fontsize=14)

# Plot Hobart on map for reference
plt.plot(147.3294, -42.8794, marker="o", lw=0, mfc='#4272f5', mec='#1438db', ms=6, zorder=20)
plt.annotate('Hobart', (147.02, -42.871), zorder=20, fontsize=14)

# Set title
plt.title('in2020_e02 CTD Deployments', fontsize=20)

# Save as SVG and cut out any white space around the plot, this is so the raw SVG can be imported into Word and
# retain its nice scaling properties. Otherwise cropping in Word changes image type and it looks ugly.
plt.savefig('C:/Users/she384/Documents/e01_dep_locations.svg', dpi=300, format='svg', bbox_inches = 'tight',
    pad_inches = 0)

# Print script run time.
finish_time = datetime.now()
print('Time elapsed: '+ str((finish_time-start_time)))
