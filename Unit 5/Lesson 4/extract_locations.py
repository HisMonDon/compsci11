location_string = "x:3,x:6,x:14,x:22"
locations = [int(loc.split(':')[1]) for loc in location_string.split(',')]
print(locations)
