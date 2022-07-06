from plotter import Plotter
from rw import get_xy_from_input, user_input, poly_csv_from_user
from geometry import Point, Line, Polygon
from create_functions import create_point_objs
from algo import categorize_points

def main():
    plotter = Plotter()
    print('read polygon.csv', '\n')
    poly_csv_input = poly_csv_from_user()
    get_xy_from_input(poly_csv_input)
    
    print('Obtain data from user', '\n')
    data = user_input()

    print('categorize point', '\n')
    Polygon20 = Polygon('poly', create_point_objs(poly_csv_input))
    cat = categorize_points(Polygon20, point_objects=data)
    
    
    print('plot polygon and point', '\n')
    xs = Polygon20.get_xs()
    ys = Polygon20.get_ys()
    plotter.add_polygon(xs, ys)
    
    x_ray = Polygon20.get_four_endpoints()[1][0]+1  #x coordinate of the other point of the ray
    for i in cat.values():
        plotter.add_point(i.get_x(), i.get_y(), i.get_category(), x_ray)
    plotter.show()
    
if __name__ == '__main__':
    main()
