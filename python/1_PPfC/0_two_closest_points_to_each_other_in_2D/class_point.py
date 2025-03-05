import csv

class point() :
    list_of_points  = []

    def __init__(self, index, x, y):
        self.x = float(x)
        self.y = float(y)
        self.index = int(index)
        point.list_of_points.append(self)
    
    def __repr__(self):
        return f"{self.index}->(X:{self.x},Y:{self.y})"
    
    @classmethod
    def instantiate_from_csv(cls):
        with open("points.csv", "r") as f :
            dict_format = csv.DictReader(f)
            list_format = list(dict_format)

        for a in list_format :
            point(
                index=int(a.get("index")),
                x=float(a.get("x")),
                y=float(a.get("y"))
            ) 
        
    @classmethod
    def point_by_index(cls, index) :
        for pt in cls.list_of_points :
            if pt.index == int(index) :
                return pt
        return None