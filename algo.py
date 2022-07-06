from geometry import Point, Line, Polygon
from create_functions import create_point_objs
polygon1 = Polygon('name', create_point_objs('polygon.csv'))
input_fp = create_point_objs('input.csv')

def on_poly_boundary(Polygon_obj, point_objects):
    """This function checks for all points that are on the boundary of the polygon and categorizes them as 'boundary'."""
    result2 = {}
    for point in point_objects:
        for line in Polygon_obj.lines():
            x1, x2, x3 = line.get_point_1().get_x(), line.get_point_2().get_x(), point.get_x()
            y1, y2, y3 = line.get_point_1().get_y(), line.get_point_2().get_y(), point.get_y()
            
            if line.cross_product(point) == 0: #This is for if a point lies on a line
                if x1 <= x3 <= x2 or x1 >= x3 >= x2:  # Point is within line range and not above or below
                    if (y3 == y1) or (0 < line.dot_product(point) < (line.distance()**2)):  # if point is on line
                        point.set_category('boundary')
                        result2[point.get_name()] = point
                        
                if y1 <= y3 <= y2 or y1 >= y3 >= y2:  # Point is within line range and not above or below
                    if x3 == x1 or 0 < line.dot_product(point) < (line.distance()**2):  # if point is on line
                        point.set_category('boundary')
                        result2[point.get_name()] = point
    return result2

def on_boundary_mbr(Polygon_obj, point_objects):
    """This function checks for all points that are on the minimum bounding rectangle but not on any of the lines of the polygon and categorizes them as 'outside'."""
    
    four_endpoints_of_poly = Polygon_obj.get_four_endpoints()
    Poly4endpoints = Polygon('poly4', [Point('end_p', i[0], i[1]) for i in four_endpoints_of_poly])
    
    result3 = {}
    for point in point_objects:
        for line in Poly4endpoints.lines():
            x1, x2, x3 = line.get_point_1().get_x(), line.get_point_2().get_x(), point.get_x()
            y1, y2, y3 = line.get_point_1().get_y(), line.get_point_2().get_y(), point.get_y()
            
            if line.cross_product(point) == 0: #This is for if a point lies on a line
                if x1 <= x3 <= x2 or x1 >= x3 >= x2:  # Point is within line  and not above or below
                    if (y3 == y1) or (0 < line.dot_product(point) < (line.distance()**2)):  # if point is on line
                        point.set_category('outside')
                        result3[point.get_name()] = point
                        
                if y1 <= y3 <= y2 or y1 >= y3 >= y2:  # Point is within line range
                    if x3 == x1 or (0 < line.dot_product(point) < (line.distance()**2)):  # if point is on line
                        point.set_category('outside')
                        result3[point.get_name()] = point
    return result3     


def mbr_outside(Polygon_obj, point_objects):
    """This function checks for the for all points that are outside the minimum bounding rectangle of the polygon and categorizes them as 'outside'."""   
    four_endpoints_of_poly = Polygon_obj.get_four_endpoints()
    
    [min_x, max_x, max_x, min_x] = [four_endpoints_of_poly[0][0], four_endpoints_of_poly[1][0], four_endpoints_of_poly[2][0], four_endpoints_of_poly[3][0]]
    [min_y, max_y, max_y, min_y] = [four_endpoints_of_poly[0][1], four_endpoints_of_poly[2][1], four_endpoints_of_poly[2][1], four_endpoints_of_poly[0][1]]
    
    result1 = {}
    for point in point_objects:
        x,y = point.get_x(), point.get_y()
        if (x<min_x or x>max_x) or (y<min_y or y>max_y): 
            point.set_category('outside')
            result1[point.get_name()] = point   
    return result1

def ray_crosses3(Polygon_obj, point_objects): 
    """This function checks for the normal cases of the ray casting algorithm, where the rays which pass through lines of 
    the polygon and not any vertices are categorized as 'outside' or 'inside' based on whether their count is even or odd"""
    result4 = {}
    for point in point_objects: 
        vertex_count = 0
        count = 0
        for line in Polygon_obj.lines():
            if (line.get_point_1().get_y() < point.get_y() < line.get_point_2().get_y()) or (line.get_point_1().get_y() > point.get_y() > line.get_point_2().get_y()):
                if (point.get_x() < line.get_point_2().get_x()) or (point.get_x() < line.get_point_1().get_x()):
                    count+=1
                else:
                    count+=0
                   # print(f'Point doesnt intersect {line}. Count is {count}')    
        
        for poly_point in Polygon_obj.get_points() :
             if point.get_x()<poly_point.get_x() and point.get_y()==poly_point.get_y(): #passes through vrtex
                   #ount+=1 #why
                    vertex_count +=1
                  #  print(f'Point passes through vertex{poly_point}.  Count is {count}')
             else: 
                count+=0
        #if-elif-else statements for normal cases...  
        if vertex_count==0 and count!=0 and count%2==0:
            point.set_category('outside')
                    
        if vertex_count==0 and count!=0 and count%2!=0:
            point.set_category('inside')
        
        if count==0 and vertex_count==0:
            point.set_category('outside')
              
        elif count==0 and vertex_count==1:
            point.set_category('inside')
                                
        elif (count==vertex_count==0):
            point.set_category('outside')    
            
        result4[point.get_name()] = point
    return result4

def special_case(Polygon_obj, point_objects):
    """This function checks for the special case of the ray casting algorithm, where the rays pass through vertices of vertical and horizontal lines of the polygon."""
    result5 = {}
    for point in point_objects:
        special_count = 0
        for line in Polygon_obj.get_horizontal_lines():
            #1. if point passes through horizontal line, special_count=0
            if (point.get_x()<line.get_point_1().get_x()) or (point.get_x()<line.get_point_2().get_x()):
                if (point.get_y()==line.get_point_1().get_y()) and (point.get_y()==line.get_point_2().get_y()):#ahould this be and or or
                    special_count+=0
                    
        #2. if point passes through vertical line, special_count+=0
        for line in Polygon_obj.get_vertical_lines():
            if (point.get_x()<line.get_point_1().get_x()) or (point.get_x()<line.get_point_2().get_x()):
                if (point.get_y()==line.get_point_1().get_y()) or (point.get_y()==line.get_point_2().get_y()):
                    special_count+=0
        #3. if passes through any other line which is non-horizontal and non-vertical, special_count+=1
        for line in [i for i in Polygon_obj.lines() if (i.get_point_1().get_x()!=i.get_point_2().get_x()) and i.get_point_1().get_y()!=i.get_point_2().get_y()]:
            if (point.get_x()<line.get_point_1().get_x() and  point.get_y()==line.get_point_1().get_y()) or (point.get_x()<line.get_point_2().get_x() and  point.get_y()==line.get_point_2().get_y()): #not within the range think vertex
                special_count+=1
        
        for line in Polygon_obj.lines():
            if (line.get_point_1().get_y() < point.get_y() < line.get_point_2().get_y()) or (line.get_point_1().get_y() > point.get_y() > line.get_point_2().get_y()):
                if (point.get_x() < line.get_point_2().get_x()) or (point.get_x() < line.get_point_1().get_x()):
                    special_count+=1
                else:
                    special_count+=0
        if special_count % 2 == 0:
            point.set_category('outside')
        else:
            point.set_category('inside')
        result5[point.get_name()] = point
    return result5


def categorize_points(Polygon_obj, point_objects):
    """Takes object of Polygon class and list of point objects from Point class as arguments and returns a dictionary with point names as keys and point objects as values."""
    
    points_on_poly_boundary = on_poly_boundary(Polygon_obj, point_objects)
    uncategorized = [i for i in point_objects if i.get_category() == False]
    print(f'{len(uncategorized)} left after running on_poly_boundary')
    
    points_on_mbr_but_outside = on_boundary_mbr(Polygon_obj, point_objects=uncategorized)
    uncategorized = [i for i in point_objects if i.get_category() == False]
    print(f'{len(uncategorized)} left after running on_boundary_mbr')
    
    points_outside_mbr = mbr_outside(Polygon_obj, point_objects= uncategorized)
    uncategorized = [i for i in point_objects if i.get_category() == False]
    print(f'{len(uncategorized)} left after running mbr_outside')
    
    uncategorized = [i for i in point_objects if i.get_category() == False]
    in_out = ray_crosses3(Polygon_obj, point_objects=uncategorized)
    final_uncategorized = [i for i in point_objects if i.get_category() == False]
    
    special = special_case(Polygon_obj, point_objects=final_uncategorized)
    final = {**points_on_poly_boundary, **points_on_mbr_but_outside, **points_outside_mbr, **in_out, **special} #merging the dicts into one
  
    final_dict = {}
    for key in sorted(final): #sorting the dict
        final_dict[key] = final[key]  
    
    return final_dict     









