from astro_pi_orbit import ISS
import time

iss = ISS()

point = iss.coordinates()
coordinates = (point.latitude.radians, point.longitude.radians)
print(coordinates)
elevation = point.elevation.km
print(elevation)

radius = elevation+6,371
