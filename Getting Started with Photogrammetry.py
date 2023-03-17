Code samples & snippets coming soon!

# Importing your 3D AR scans to your workspace
# Import libraries
import arcpy
from arcpy import env

arcpy.CheckOutExtension("3D")
env.workspace = "C:/data"
arcpy.Import3DFiles_3d("AddAR.skp", "Test.gdb/AddAR", False, "", False)
