import os


def cls() :
    os.system("cls" if os.name=="nt" else "clear")

def dist_between(x1, x2, y1, y2) :
    return float((((float(x1)-float(x2))**2) + ((float(y1)-float(y2))**2))**0.5)

def check_if_point_in_rectangle(x1, y1, xcheck, ycheck, rect_x, rect_y) :
    if xcheck>=(x1-rect_x/2) and xcheck<=(x1+rect_x/2) and ycheck>=(y1-rect_y/2) and ycheck<=(y1+rect_y/2) :
        return True
    else :
        return False
    """
        These Checks do work
            print(check_if_point_in_rectangle(1,2,3,2,2,6)) #True
            print(check_if_point_in_rectangle(1,2,1,0,2,6)) #False
    """

