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

rect_x = abs(point.point_by_index(0).x - point.point_by_index(1).x) * 2
rect_y = abs(point.point_by_index(0).y - point.point_by_index(1).y) * 2

list_of_points_inside_the_rectangle = []
check_dictionary = dict()

total_checks = 0




while (1) :
    something_changed = False
    for i in range(config.num_of_points) :
        for j in range(i+1, config.num_of_points) :
            
            if check_dictionary.get(frozenset([i,j])) == False :
                continue
            
            total_checks += 1

            if check_if_point_in_rectangle(point.point_by_index(i).x, point.point_by_index(i).y, point.point_by_index(j).x, point.point_by_index(j).y, rect_x, rect_y) == True :
                if config.toggle_debug :
                    print(f"{i} encloses {j} at rect x,y  {rect_x:.2f} {rect_y:.2f}")
                
                check_dictionary[frozenset([i, j])] = True

                #To take into account multiple points with same distance.
                if(
                    len(list_of_points_inside_the_rectangle)!=0 and
                    dist_between(
                        point.point_by_index(i).x,
                        point.point_by_index(j).x,
                        point.point_by_index(i).y,
                        point.point_by_index(j).y
                    ) 
                    ==
                    dist_between(
                        point.point_by_index(list_of_points_inside_the_rectangle[0][0]).x,
                        point.point_by_index(list_of_points_inside_the_rectangle[0][1]).x,
                        point.point_by_index(list_of_points_inside_the_rectangle[0][0]).y,
                        point.point_by_index(list_of_points_inside_the_rectangle[0][1]).y
                    )
                ) :
                    list_of_points_inside_the_rectangle.append([i,j])
                
                else :
                    list_of_points_inside_the_rectangle.clear()
                    list_of_points_inside_the_rectangle.append([i,j])

                something_changed = True
            
            else :
                check_dictionary[frozenset([i, j])] = False
            

            # Shrink rectangle **only if something changed**
    if something_changed:
        if config.toggle_debug :
            print("------")
        rect_x *= 1 - config.rectangle_decrement_percent
        rect_y *= 1 - config.rectangle_decrement_percent
    else:
        # If nothing changed, print results and quit
        print(list(map(list, set(map(tuple, list_of_points_inside_the_rectangle)))), 
              f" At dist: {dist_between(  
                  point.point_by_index(list_of_points_inside_the_rectangle[0][0]).x,
                  point.point_by_index(list_of_points_inside_the_rectangle[0][1]).x,
                  point.point_by_index(list_of_points_inside_the_rectangle[0][0]).y,
                  point.point_by_index(list_of_points_inside_the_rectangle[0][1]).y
              ):.3f}")
        if config.toggle_debug :
            print(f"Total Checks = {total_checks}")
        quit()

