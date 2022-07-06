from collections import OrderedDict

import matplotlib
import matplotlib.pyplot as plt

# if plotting does not work comment the following line
matplotlib.use('TkAgg')


class Plotter:

    def __init__(self):
        plt.figure()
    
    def add_polygon(self, xs, ys):
        plt.fill(xs, ys, 'lightgray', label='Polygon')
        
    def add_point(self, x, y, kind=None, x_ray=None):
        if kind == 'outside':
            plt.plot(x, y, 'ro', label='Outside')
            plt.plot([x, x_ray], [y, y])
        elif kind == 'boundary':
            plt.plot(x, y, 'bo', label='Boundary')
            plt.plot([x, x_ray], [y, y])
        elif kind == 'inside':
            plt.plot(x, y, 'go', label='Inside')
            plt.plot([x, x_ray], [y, y])
        else:
            plt.plot(x, y, 'ko', label='Unclassified')
            plt.plot([x, x_ray], [y, y])
    
    def show(self):
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys())
        plt.show()
