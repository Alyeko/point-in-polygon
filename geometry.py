class Geometry:
    def __init__(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_name(self):
        pass
    
    def __repr__(self):
        pass
    
class Point(Geometry):
    def __init__(self, name, x, y, category=False):
        super().__init__(name)
        self.__x = x
        self.__y = y
        self.__category = category
        
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def get_xy(self):
        return self.__x,self.__y
    
    def set_category(self, category):
        self.__category = category
    
    def get_category(self):
        return self.__category 
    
    def __add__(self, other):
        return(self.get_x() + other.get_x(), self.get_y() + other.get_y()) 
    
    def __repr__(self):
        return f'POINT({self.__x},{self.__y})'
   
        
class Line(Geometry):
    def __init__(self, name, point_1, point_2):
        super().__init__(name)
        self.__point_1 = point_1
        self.__point_2 = point_2
        
    def get_point_1(self):
        return self.__point_1
    
    def get_point_2(self):
        return self.__point_2
    
    def distance(self):
        return (((self.__point_2.get_x()-self.__point_1.get_x())**2) + ((self.__point_2.get_y()-self.__point_1.get_y())**2)) ** 0.5
    
    def cross_product(self, point):
        """Calculates  the cross product of a line and a point"""
        return (point.get_y() - self.__point_1.get_y()) * (self.__point_2.get_x() - self.__point_1.get_x()) - (point.get_x() - self.__point_1.get_x()) * (self.__point_2.get_y() - self.__point_1.get_y())
        
    def dot_product(self, point):
        """ """
        return (point.get_x() - self.__point_1.get_x()) * (self.__point_2.get_x() - self.__point_1.get_x()) + (point.get_y() - self.__point_1.get_y())*(self.__point_2.get_y() - self.__point_1.get_y())
    
    def __repr__(self):
        return f'LINE({self.__point_1.get_x(),self.__point_1.get_y()},{self.__point_2.get_x(),self.__point_2.get_y()})'
    
    def on_line_segment(self, point): #self is a line which has point1 and point2
        """Checks if q lies on the segment pr""" 
        p = self.__point_1
        r = self.__point_2
        q = point
        
        if ((q.get_x() <= max(p.get_x(), r.get_x())) and (q.get_x() >= min(p.get_x(), r.get_x())) and
               (p.get_y() <= max(p.get_y(), r.get_y())) and (q.get_y() >= min(p.get_y(), r.get_y()))):
            return True
        return False

   

class Polygon(Geometry):
    """The points argument must be a list of point objects!
       Simply loop through a list of ordinary (x,y) values and create Point objects out of them before passing them into the 
       Polygon class to create one"""
       
    def __init__(self, name, points):
            super().__init__(name)
            self.__points = points
            self.__filepath = False
                
    def get_points(self):
        return self.__points
    
    def get_xs(self):
        xs = [i.get_x() for i in self.get_points()]
        return xs

    def get_ys(self):
        ys = [i.get_y() for i in self.get_points()]
        return ys
    
    def set_poly_name(self, filepath): #need to fix this, doesnt work well
        try:
            poly_name = input('Enter a name for your polygon or hit ENTER to use the same name of the file: ')
            if poly_name == '':
                print('User wants the same name as file!')
                saved_args = locals()
                filename = saved_args['filepath']
                file_objs = filepath.split('/')
                if len(file_objs) > 1:       #I WANT TO MAKE THIS A CLASS SO HAT I CAN DEF A METHOD GT_FILENAME FROM WHT  THE USER HA INPUTED
                    filename = file_objs[-1]
                else:
                    filename = file_objs[0]
                poly_name = filename.split('.')[0]
        
            else:
                print('User entered a preferred name!')
            
            return poly_name
        except TypeError as e:
            print('Enter the filpath of your polygon')
        return self.get_name()
    
    def lines(self): #should this be lines or get_lines
        res = []
        points = self.get_points()
        point_a = points[0]
        for point_b in points[1:]:
            res.append(Line(str(point_a.get_name()) + '-' + str(point_b.get_name()), point_a, point_b))
            point_a = point_b 
        res.append(Line(str(point_a.get_name()) + '-' + str(points[0].get_name()), point_a, points[0]))
        return res   
    
    def get_vertical_lines(self):
        vertical_lines = [line for line in self.lines() if line.get_point_1().get_x()==line.get_point_2().get_x()][:-1] #excluding the last point because it is the same point
        return vertical_lines
    
    def get_horizontal_lines(self):
        horizontal_lines = [line for line in self.lines() if line.get_point_1().get_y()==line.get_point_2().get_y()][:-1] #excluding the last point because it is the same point
        return horizontal_lines
    
    def get_four_endpoints(polygon_obj):
        """Polygon object must be passed as argument"""
        #need to check if the object passed is a polygon...
       # if not isinstance(point, Point):
       #     Point(point)
       # poly_points_list = create_point_obj_from_filepath(filepath) #gives us a list of points objects created from our filepath
    
        min_x = 100000 # start with something much higher than expected min
        min_y = 100000
        max_x = -100000 # start with something much lower than expected max
        max_y = -100000

        for item in polygon_obj.get_points():
            if item.get_x() < min_x:
                min_x = item.get_x()

            if item.get_x() > max_x:
                max_x = item.get_x()

            if item.get_y() < min_y:
                min_y = item.get_y()

            if item.get_y() > max_y:
                max_y = item.get_y()
        return [(min_x,min_y),(max_x,min_y),(max_x,max_y),(min_x,max_y)]

    
    
    def __repr__(self):
        pass
        reprr = []
        pointss = self.get_points()
        for point in pointss:
            reprr.append(point.get_xy()) 
        reprr.append(pointss[0].get_xy())
        return f'POLYGON{reprr}'
