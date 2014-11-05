__author__ = 'sleonard'
#Write a script that creates a 15,000-meter buffer around features in the airports.shp feature class classified as an
# airport ( based on the FEATURE field ) and a 7,500-meter buffer around features classified as a seaplane base

import arcpy
from arcpy import env
env.workspace = "F:/GIS/A_Masters_Program/Python/Data/Exercise07"
# define working file
fecl = "airports.shp"
# define variables for selecting out Airports and seaplane bases
var1 = "\"FEATURE\" = 'Airport'"
var2 = "\"FEATURE\" = 'Seaplane Base'"
# the next two steps select out the variables and create new shapefiles.
arcpy.Select_analysis(fecl, "Results/airport_15000M.shp", var1)
arcpy.Select_analysis(fecl, "Results/airport_7500M.shp", var2 )
# final steps take the just created files and builds buffers and outputs two new shapefiles.
arcpy.Buffer_analysis("Results/airport_15000M.shp", "Results/airports_buffer_15000M.shp", "15000 METERS")
arcpy.Buffer_analysis("Results/airport_7500M.shp", "Results/airports_buffer_7500M.shp", "7500 METERS")
