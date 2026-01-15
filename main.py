from astro_pi_orbit import ISS
import numpy as np
import time
import matplotlib.pyplot as plt
import math

def getPointData(initialTime = 0.):
    iss = ISS()

    point = iss.coordinates()
    lat, lon, alt =point.latitude.radians, point.longitude.radians, point.elevation.km

    # works out the radius of earth at a specific point
    f = 0.003352810642
    radius = 6378.137*(1 - f*(math.sin(lat)**2))

    distFromO = radius+alt

    return np.array([lat, lon, distFromO, time.time()-initialTime])

# variables
sleepTime = 5
sampleNum = 2

dataList = np.zeros(shape=(sampleNum, 4))
startTime = time.time()
for x in range(0, sampleNum):
    dataList[x] = getPointData(startTime)
    time.sleep(sleepTime)

# speed calc testing
dLat = dataList[0, 0] - dataList[1, 0]
dLon = dataList[0, 1] - dataList[1, 1]
dAngle = math.pow(math.pow(dLat, 2) + math.pow(dLon, 2), 0.5)
distTravelled = dAngle * dataList[0, 2]
speed = distTravelled / (dataList[1, 3] - dataList[0, 3])
print(f"speed = {speed*3600} km/h")

# plotting for testing
plt.plot(dataList[:,3], dataList[:,2])
plt.ticklabel_format(useOffset=False)
plt.show()