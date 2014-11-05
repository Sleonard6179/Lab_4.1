__author__ = 'sleonard'
import arcpy
from arcpy import env
#set workspace
env.workspace = "G:/Python/Data/Exercise05"
env.overwriteOutput = True
# set variables
toBeDissolved = "parks.shp"
dissolveFinished = "Results/parks_dissolve.shp"
dissolveField = "PARK_TYPE"

# Execute Dissolve
arcpy.Dissolve_management(toBeDissolved, dissolveFinished, dissolveField,"", "SINGLE_PART", "")
