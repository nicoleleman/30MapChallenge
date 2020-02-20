import networkx as nx
import osmnx as ox
import requests
import matplotlib.cm as cm
import matplotlib.colors as colors

# gdf = ox.gdf_from_places(['United Kingdom', 'Ireland'])
# gdf = ox.project_gdf(gdf)
# fig, ax = ox.plot_shape(gdf)

G = ox.graph_from_place('Greater London', network_type='drive')
fig, ax = ox.plot_graph(G)