import os
import csv
import config
from class_point import *
from functions import *



"""
    Main Body
"""
#Clear Screen
if config.toggle_clear_screen :
    cls()

#Instantiating from CSV
point.instantiate_from_csv()

# print(point.list_of_points)
# print(point.point_by_index("0").x)

min_dist = float('inf')
closest_index = [0,0]
for i in range(config.num_of_points) :
    for j in range(i+1, config.num_of_points) :
        temp = dist_between(point.point_by_index(i).x, point.point_by_index(j).x, point.point_by_index(i).y, point.point_by_index(j).y)
        if config.toggle_debug  :
            print(f"Checking {i}-{j}, Distance: {temp :.2f}")
        if  temp < min_dist :
            min_dist = temp
            closest_index.clear() 
            closest_index.append([i,j])
        elif temp == min_dist :
            closest_index.append([i,j])
    
print(closest_index, " At Dist :", f"{min_dist:.3f}")