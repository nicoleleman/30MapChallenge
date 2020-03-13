import networkx as nx
import csv
import pandas as pd
import osmnx as ox
import requests
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
inner_london_boroughs = ['City and County of the City of London',
                             'London Borough of Camden, London',
                             'Royal Borough of Greenwich, London',
                             'London Borough of Hackney, London',
                             'London Borough of Hammersmith and Fulham, London',
                             'London Borough of Islington, London',
                             'Royal Borough of Kensington and Chelsea, London',
                             'London Borough of Lambeth, London',
                             'London Borough of Lewisham, London',
                             'London Borough of Southwark, London',
                             'London Borough of Tower Hamlets, London',
                             'London Borough of Wandsworth, London',
                             'City of Westminster, London']


longitude = []
latitude = []
with open('Pubs.csv', 'r') as long_lat:
    reader = csv.reader(long_lat)
    next(reader, None)
    for row in reader:
        longitude.append(row[10])
        latitude.append(row[11])

G = ox.graph_from_place('London Borough of Southwark, London')
fig, ax = ox.plot_graph(G, show=False, close=False, node_size=1)
ax.scatter(-0.071038176, 51.4735944, s=20, c='red')
plt.show()

'''
Testing code
'''
# G = ox.graph_from_address('1600 Pennsylvania Ave NW, Washington, DC 20500', distance=1000)
# fig, ax = ox.plot_graph(G, show=False, close=False)
# ax.scatter(-77.036498, 38.897270, c='red')
# plt.show()

# G = ox.graph_from_place('London Borough of Southwark, London' , network_type='drive', retain_all=True)
# pub = ox.get_nearest_node(G, (-0.071038176, 51.4735944))
# ax.scatter(-0.071038176, 51.4735944, c='red')
# fig, ax = ox.plot_graph(G, show=False, close=False)
# ox.get_nearest_node(G, (39.982066, -81.11861))
# ox.plot_graph_route(G, [ox.get_nearest_node(G, (39.982066, -81.11861))])
