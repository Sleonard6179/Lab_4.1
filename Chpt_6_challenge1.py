__author__ = 'sleonard'
import arcpy
from arcpy import env
env.workspace = "F:/GIS/A_Masters_Program/Python/Data/Exercise06"
env.overwriteOutput = True
# Write a script that reads all feature classes in a workspace and prints the name of each feature class and the
#   geometry type of that feature class.
wrkspc = "F:/GIS/A_Masters_Program/Python/Data/Exercise06"
fun1 = arcpy.ListFeatureClasses()

for i in fun1:
    desc1 = arcpy.Describe(i)
    print desc1.basename + " is a " + desc1.shapeType