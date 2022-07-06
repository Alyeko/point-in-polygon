"""Function in this file can be called into other progammes to read and write files """
def read_csv(filepath):#should this take filename or filepath...
    with open(filepath, 'r') as f:
        data = f.read()
    data = data.split('\n')
    if data[-1] == '':
        data.pop(-1)
    else:
        data
        
    data_wo_headers = data[1:] #ignoring the header columns
    data = [[float(num) for num in entry.split(',')] for entry in data_wo_headers]
    return data


def pt_get_xy_from_input(filepath):#mm when can i use this
    xy = {}
    for row in read_csv(filepath):
        xy[f'Point{int(row[0])}'] = (row[1], row[2])
        locals().keys()
    return xy   #should this return keys and values


def get_xy_from_input(filepath):
    """Returns a dictionary with id value sas keys and tuple of xy coordinates as values
    Maybe add an example..."""
    xy = {}
    for row in read_csv(filepath):
        xy[int(row[0])] = (row[1], row[2])
        locals().keys() #why this?? for the filepaths?? filename?? for the set_name in the geometry class functions?/
    return xy   #should this return keys and values


def get_xs_from_input(filepath):
    xs = [row[1] for row in read_csv(filepath)]
    return xs


def get_ys_from_input(filepath):
    ys = [row[2] for row in read_csv(filepath)]
    return ys


def poly_csv_from_user():
    """1. Asks for filepath from user which must be csv.
       2. Returns the filepath passed"""
    try:
        user_filepath = input('Enter filepath of polygon csv (without quotes): ')        
        return user_filepath
    except FileNotFoundError as f:
        raise Exception('Invalid Filepath passed.') from None
        
        
def points_csv_from_user():
    """1. Asks for filepath from user which must be csv.
       2. Returns the filepath passed"""
    try:
        user_filepath = input('Enter filepath of point csv (without quotes): ')        
        return user_filepath
    except FileNotFoundError as f:
        raise Exception('Invalid Filepath passed.') from None   
        
   
def user_input():
    """"""
    from geometry import Point
    from create_functions import create_point_objs, check_input_type
    try:
        choice = int(input('-----------CHOICES---------------''\n''1. Enter one point''\n''2. Enter two points maximum: ''\n'))
        if choice == 1:
            #call user_input function here.. which returns point object...
            print('\n''Insert point information')
            x = float(input('x coordinate: ')) #error handling for invalid inputs of x and y. do that
            y = float(input('y coordinate: '))

            while True:
                name = input('Enter point name: ')
                if check_input_type(name) == 'float':
                    print('Invalid name passed. Point names must not be floats and no spaces: ')
                else: 
                    break
            print('name stored!')
           # print(name)
            data_from_user = [Point(name, x, y)]

        elif choice == 2:
            points_info = input('Enter names and 2 x-y pairs of coordinates, separated by space: ''Here\'s an example''\n' 'Point1(x1,y1) Point2(x2,y2): ')
            pi = points_info.split()
            p_list = []
            pi_splitted_list = [pi[i] for i in range(len(pi))]
            for i in pi_splitted_list:
                p_list.append((i[0:i.index('(')], float(i[i.index('(')+1:i.index(',')]), float(i[i.index(',')+1:i.index(')')])))
            
            data_from_user = create_point_objs(p_list)

        else:
            print('Invalid choice passed, Choices can only be 1 or 2.')

    except ValueError as v:
        raise Exception(f'Invalid input. Choices cannot be strings, can only be 1 or 2') from None #code adapted from an answer from https://stackoverflow.com/questions/52725278/during-handling-of-the-above-exception-another-exception-occurred

    return data_from_user


def write_file(filepath, dictionary):##do you really need to tae a dict as argument... also the dictonary here willfrom the categorization functions ie mbr and rca   
    with open(filepath, 'w') as f: 
        for key, value in dictionary.items(): 
            f.write(f'{key},{value.get_category()}\n') 
        print('Output written to file')
    return 'Output written to file'
