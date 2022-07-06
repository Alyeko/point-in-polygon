from geometry import Point, Line, Polygon
from rw import get_xy_from_input

def create_point_objs(filepath):
    """Takes filepath as argument and returns a list of points objects for all points that were in that file in the filepath"""
    if isinstance(filepath, str) and filepath.endswith('.csv'): 
        keys = [i for i in get_xy_from_input(filepath).keys()]
        values = [i for i in get_xy_from_input(filepath).values()]
        point_list = []
        for i in zip(keys, values):
            Point(i[0], i[1][0], i[1][1])
            point_list.append(Point(i[0], i[1][0], i[1][1]))
         
    elif isinstance(filepath, list):          
        point_list = []
        for i in filepath:
            point_list.append(Point(i[0], i[1], i[2]))
            
    elif isinstance(filepath, dict):
        point_list = []
        for i in filepath.items():
            point_list.append(Point(i[0], i[1][0], i[1][1]))
    return point_list

def create_line():
    pass

def create_polygon(filepath):
    points = create_point_objs(filepath)
    return Polygon('Polygon', points)

def check_input_type(input_str):
    """Code adapted from https://pynative.com/python-check-user-input-is-number-or-string/"""
    if input_str.strip().isdigit():
        return 'integer'
    elif input_str.strip().isalnum():
        return 'alnum'
    elif input_str.strip().isnumeric()==False:
        return 'float'
    else:
        return 'string'
