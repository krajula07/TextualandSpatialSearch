from pymongo import MongoClient
from pymongo.collation import Collation
import os
import sys
import json
import math
import re


def FindBusinessBasedOnCity(cityToSearch, saveLocation1, collection):
    #pass
    tb = collection .find({"city" : re.compile('^' + cityToSearch + '$', re.IGNORECASE)})
    location = saveLocation1
    oFile = open(location, 'w')   
    for location in tb:
        loc_name = location["name"].upper()
        loc_address = location["full_address"].upper()
        loc_city = location["city"].upper()
        loc_state = location["state"].upper()
        loc_line = loc_name + "$" + loc_address + "$" + loc_city + "$" + loc_state + "\n"
        oFile.write(loc_line)
    oFile.close()
        

    
def Distance_algo(latitude_2, longitude_2, latitude_1, longitude_1):
    R = 3959
    x1 = math.radians(latitude_1)  
    x2 = math.radians(latitude_2) 
    latitude_difference = (latitude_2-latitude_1)
    dLatitude = math.radians(latitude_difference)
    longitude_difference = (longitude_2 - longitude_1)
    dLongitude = math.radians(longitude_difference)  
    cal = (math.sin(dLatitude/2)*math.sin(dLatitude/2)) + (math.cos(x1)*math.cos(x2) * math.sin(dLongitude/2)*math.sin(dLongitude/2))
    fCal = 2 * math.atan2(math.sqrt(cal), math.sqrt(1-cal))  
    distance = R * fCal   
    return distance
    

def FindBusinessBasedOnLocation(categoriesToSearch, myLocation, maxDistance, saveLocation2, collection):
    #pass
    tb = collection.find({ "categories" : {"$in" : categoriesToSearch} })   
    lat = myLocation[0]
    latitude = float(lat)
    long = myLocation[1]
    longitude = float(long)
    mDis = float(maxDistance)
    File_location = saveLocation2
    oFile = open(File_location, 'w')     
    for location in tb:
        loc_name = location["name"].upper()
        loc_longitude = location["longitude"]
        loc_fLongitude = float(loc_longitude)
        loc_latitude = location["latitude"]
        loc_fLatitude = float(loc_latitude)
        dCalculation = Distance_algo(latitude, longitude, loc_fLatitude, loc_fLongitude)
        dFCalculation = abs(dCalculation)
        if (dFCalculation <= mDis):
            oFile.write(loc_name)
            oFile.write("\n")
    oFile.close()
    

