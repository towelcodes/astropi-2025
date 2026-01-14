from astro_pi_orbit import ISS
import time

def getPointData():
    iss = ISS()

    point = iss.coordinates()
    return point.latitude.radians, point.longitude.radians, point.elevation.km

print(getPointData())
