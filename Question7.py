import arcpy 

arcpy.env.workspace = r'C:\Users\theyduk\Desktop\Heyduk_LabWork\610 Assignments\610 Exercise 3\Exercise 3.gdb'
arcpy.env.overwriteOutput = True 

inFeatures = r'C:\Users\theyduk\Desktop\Heyduk_LabWork\610 Assignments\610 Exercise 3\Exercise 3.gdb\CallsforService'

outLocation = 'FeaturetoFeature'

arcpy.MakeFeatureLayer_management(inFeatures, 'CallsforService_lyr')

arcpy.SelectLayerByAttribute_management('CallsforService_lyr','NEW_SELECTION',"CFSType = 'Assault Call'")

arcpy.CopyFeatures_management('CallsforService_lyr',r'C:\Users\theyduk\Desktop\Heyduk_LabWork\610 Assignments\610 Exercise 3\Exercise 3.gdb\New_Selection')

     