__author__ = 'sleonard'
# Write a script that runs the Add XY Features on the hospital.shp feature class.
#
#
import arcpy
from arcpy import env
#set workplace
env.workspace = "G:/Python/Data/Exercise05"
env.overwriteOutput = True
# Set local variables
In_data = "hospitals.shp"
out_data = "Results\\hospitals_copy.shp"

# Copy data to preserve original data set.
arcpy.Copy_management(In_data, out_data)

#Execute addXY
arcpy.AddXY_management(out_data)