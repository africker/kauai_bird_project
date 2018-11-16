#kauaiRasterExtract.py
import arcpy, sys, os
arcpy.env.overwriteOutput=True
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
arcpy.CheckOutExtension("Highways")
arcpy.env.overwriteOutput=True


InFolder = r"D:\OneDrive - California Polytechnic State University\02_RESEARCH_PROJECTS\07_KAUAI_BIRDS\GIS\RASTER\CLIMATE_DATA\monthlyData"
base_root = r"D:\OneDrive - California Polytechnic State University\02_RESEARCH_PROJECTS\07_KAUAI_BIRDS\GIS\RASTER\CLIMATE_DATA"
outFolder = r"D:\02_SANDBOX\kauai_staging\outDBF"

rasters = arcpy.ListRasters()
inZoneData  = r"D:\02_SANDBOX\kauai_staging\2018_Kauai_FB_PointCountLocations_50mBuffer.shp"
workspace = InFolder
zoneField = "FID"
rasters = []  
walk = arcpy.da.Walk(workspace, type="GRID") #was "GRID" originally to convert to tif
for dirpath, dirnames, filenames in walk:
    for filename in filenames:
        rasters.append(os.path.join(dirpath, filename))  
for raster in rasters:
    fileNameParts = raster.split('\\')
    print(fileNameParts)
    print(fileNameParts[-1])
    print(raster)
    outRaster = raster + ".tif"
    arcpy.CopyRaster_management(raster,outRaster,"", "", "-3.402823e+38", "NONE", "NONE", "32_BIT_FLOAT", "NONE", "NONE", "TIFF", "NONE")
    outTable = outFolder + os.sep + fileNameParts[-1] + ".dbf"
    outZSaT = ZonalStatisticsAsTable(inZoneData, zoneField, raster, outTable, "NODATA", "ALL")
    print("output table:  " + str(outZSaT))
    #outZSaT = ZonalStatisticsAsTable(inZoneData, zoneField, raster, outTable, "NODATA", "MEAN")
"""
months = []
for dirpath, dirnames, filenames in walk:
    for dir in dirnames:
months.append(os.path.join(dirpath,dir))

for month in months:
    fileNameParts = month.split('\\')  
    env.workspace = month  
    rasters = arcpy.ListRasters()  
    print(month) 
    for raster in rasters:
        #print(raster)
        outRaster = "\\"+raster + ".tf"
        print(outRaster)
        arcpy.CopyRaster_management(raster,outRaster,"", "", "-3.402823e+38", "NONE", "NONE", "32_BIT_FLOAT", "NONE", "NONE", "TIFF", "NONE")
"""
