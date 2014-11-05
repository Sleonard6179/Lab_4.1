__author__ = 'sleonard'
import arcpy
from arcpy import env
env.workspace = "F:/GIS/A_Masters_Program/Python/Data/Exercise06/Results/NM.gdb"
env.overwriteOutput = True
# Write a script that reads all the feature classes in a personal or file geodatabase and copies only
#  the polygon feature classes to a new file geodatabase.
list = arcpy.ListFeatureClasses()
arcpy.CreateFileGDB_management("F:/GIS/A_Masters_Program/Python/Data/Exercise06/Results", "New_database.gdb")
for poly in list:
    desc = arcpy.Describe(poly)
    if desc.shapeType == "Polygon":
        arcpy.Copy_management (poly,"F:/GIS/A_Masters_Program/Python/Data/Exercise06/Results/New_database.gdb/" + poly)