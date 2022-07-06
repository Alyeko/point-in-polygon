from plotter import Plotter
from rw import get_xy_from_input, write_file, poly_csv_from_user, points_csv_from_user
from create_functions import create_polygon, create_point_objs
from geometry import Point, Line, Polygon
from algo import categorize_points


def main():
    plotter = Plotter()
    
    print('read polygon.csv')
    poly_csv_input = poly_csv_from_user()
    get_xy_from_input(poly_csv_input)
    
    print('read input.csv')
    points_csv_input = points_csv_from_user()
    get_xy_from_input(points_csv_input)

                
    print('categorize points')
    Polygon20 = create_polygon(get_xy_from_input(poly_csv_input))
    input_points100 = create_point_objs(get_xy_from_input(points_csv_input))
    cat = categorize_points(Polygon20, point_objects=input_points100)
    print([i.get_category() for i in cat.values()])

    print('write output.csv')
    write_file('final_output.csv', cat)
    
    print('plot polygon and points')    
    #polygon_obj = create_polygon('polygon.csv')
    xs = Polygon20.get_xs()
    ys = Polygon20.get_ys()
    plotter.add_polygon(xs, ys)
    
    
    outside= [i for i in cat.values() if i.get_category()=='outside']
    boundary=[i for i in cat.values() if i.get_category()=='boundary'] 
    inside = [i for i in cat.values() if i.get_category()=='inside']
    special = [i for i in cat.values() if i.get_category()==False]
    for i in boundary:
        plotter.add_point(i.get_x(), i.get_y(), kind='boundary')
    for g in outside:
        plotter.add_point(g.get_x(), g.get_y(), kind='outside')
    for j in inside:
        plotter.add_point(j.get_x(), j.get_y(), kind='inside')
    for k in special:
        plotter.add_point(k.get_x(), k.get_y(), kind=k.get_category())
        
    plotter.show()
   
if __name__ == '__main__':
    main()
