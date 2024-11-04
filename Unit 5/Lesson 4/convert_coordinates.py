coordinate_string = "x:2,y:5 - x:5,y:11 - x:7,y:14"
coordinates = []
for coord in coordinate_string.split(' - '):
    x, y = coord.split(',')
    x_val = int(x.split(':')[1])
    y_val = int(y.split(':')[1])
    coordinates.append([x_val, y_val])
print(coordinates)
