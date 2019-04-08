#KFBRP Kernel Density Calculator
import arcpy, os
from arcpy import env
from arcpy.sa import *
from datetime import datetime

start=datetime.now()
start_str = str(start)
print("program start date, time = " + start_str)
arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension("Spatial")

#Edit the coordinates XMin, YMin, XMax, YMax
arcpy.env.extent = "432270 2439130 446180 2450480"

#Parameters
inFolder = r"D:\OneDrive - California Polytechnic State University\02_RESEARCH_PROJECTS\07_KAUAI_BIRDS\MAXENT\inputPoints\2019_Analysis\shp"
env.workspace = inFolder
scales = ['10', '100', '250']
outFolder = r"D:\OneDrive - California Polytechnic State University\02_RESEARCH_PROJECTS\07_KAUAI_BIRDS\MAXENT\inputPoints\2019_Analysis\kernelDensity"
populationField = "NONE"
searchRadius = 2500 #might need to change this later

fcs = arcpy.ListFeatureClasses()
for fc in fcs:
    print(fc)
    fcName = fc[:-4]
    print(fcName)
    for scale in scales:
        print(scale)
        cellSize = scale
        outKernelDensity = KernelDensity(fc, populationField, cellSize,
                                 "","SQUARE_METERS")
        outName = fcName + "_" + scale + "_kd_nsr.tif"
        outKernelDensity.save(outFolder + os.sep + outName)

print ('All kernel density rasters calculated')  
finish = datetime.now() 
finish_str = str(finish)
print("program finish date, time = %s" % finish_str)
totaltime = finish-start
print ('total processing time = %s' % totaltime)    


