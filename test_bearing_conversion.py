
def deg_to_compass(deg):
    deg = deg % 360
    dir_arr = ["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
    num_compass_headings = len(dir_arr)
    deg_per_compass_heading = 360/num_compass_headings
    idx = int((deg/deg_per_compass_heading)+.5) % num_compass_headings
    return dir_arr[idx]

def deg_to_compass2(deg):
    deg = deg % 360
    dir_arr = ["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
    idx = int((deg + 11.25)/22.5) % len(dir_arr)
    return dir_arr[idx]

for i in range(-720,720):
    failures = 0
    old = deg_to_compass(i)
    new = deg_to_compass2(i)
    if old != new:
        failures += 1
        print(i,old,new)

if failures == 0:
   print("No failures")

