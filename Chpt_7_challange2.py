__author__ = 'sleonard'
#Write a script that adds a text field to the roads.shp feature class called FERRY and populates this field
# with YES and NO values, depending on the value of the FEATURE field
#
#Set up workspace
import arcpy
from arcpy import env
env.workspace = "F:/GIS/A_Masters_Program/Python/Data/Exercise07"
#working file
workFile = "roads.shp"
# add a new text field
field1 = "FERRY"
arcpy.AddField_management(workFile, field1,"TEXT", "", "", 10)
# build Cursor
cursor = arcpy.da.UpdateCursor(workFile, ["FEATURE", field1])
# I stole this from the cheat sheet, I couldn't figure this last part out.
for row in cursor:
    if row[0] == "Ferry Crossing":
        row[1] = "YES"
    else:
        row[1] = "NO"
    cursor.updateRow(row)