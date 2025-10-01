from astro_pi_orbit import ISS

iss = ISS()

point = iss.coordinates()
coordinates = (point.latitude, point.longitude)
print(coordinates)
elevation = point.elevation.km
print(elevation)