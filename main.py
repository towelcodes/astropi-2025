from astro_pi_orbit import ISS
import numpy as np
import time

def getPointData():
    iss = ISS()

    point = iss.coordinates()
    return np.array([point.latitude.radians, point.longitude.radians, point.elevation.km, time.time()])

sampleNum = 5


dataList = np.zeros(shape=(sampleNum, 4))
for x in range(0, sampleNum):
    dataList[x] = getPointData()
    time.sleep(10)
print(dataList[:,2])