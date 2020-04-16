import osmnx as ox
from IPython.display import Image

# configure the inline image display
city_list = ['London, United Kingdom', '5th Avenue, New York City', 'Placa de Tetuan, Barcelona', 'Central, Hong Kong']

def create_map(list):
    for city in list:
        img_folder = 'images'
        extension = 'png'
        size = 300
        dpi = 150
        fig, ax = ox.plot_figure_ground(address=city, filename=city, dpi=dpi)
        Image('{}.{}'.format(city, extension), height=size, width=size)

create_map(city_list)