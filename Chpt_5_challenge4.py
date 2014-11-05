__author__ = 'sleonard'
import arcpy
from arcpy import env
#set workspace
env.workspace = "G:/Python/Data/Exercise05"
env.overwriteOutput = True
# Check for Extensions
ext_available = ["3D", "Schematics","ArcScan", "Business", "DataInteroperability", "GeoStats", "JTX", "Network", "Aeronautical", "Defense","Foundation","Datareviewer", "Nautical", "Spatial", "StreetMap", "Tracking" ]
for i in ext_available:
    if arcpy.CheckExtension(i) == "Available":
        print "You totally have the extension " + i + "; Rock the F**k on!"
    else:
        print "OH f**k you ain't got the extension " + i + "; Sad Panda :( "