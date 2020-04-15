import osmnx as ox
from IPython.display import Image

# configure the inline image display
def create_map():
    img_folder = 'images'
    extension = 'png'
    size = 300
    dpi = 150
    place = 'london'
    point = (51.510244, -0.138130)
    fig, ax = ox.plot_figure_ground(point=point, filename=place, dpi=dpi)
    Image('{}.{}'.format(place, extension), height=size, width=size)

create_map()