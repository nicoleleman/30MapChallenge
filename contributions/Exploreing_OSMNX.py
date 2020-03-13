import networkx as nx
import osmnx as ox
import requests
import matplotlib.cm as cm
import matplotlib.colors as colors

def get_inner_london():
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
    inner_london = ox.gdf_from_places(inner_london_boroughs, gdf_name='london')
    G = ox.graph_from_place(inner_london_boroughs, network_type='drive', retain_all=True)
    # Plots a map of inner London with drivable streets
    fig, ax = ox.plot_graph(G, save=True, filename='inner_london_roads')
    print(inner_london)

def draw_colourcoded_map():
    borough_name = input("Enter area name:")
    print('Colouring map of:' + borough_name)
    def colourcode(x):
        if ('street' in x):
            return '#f10000'
        elif ('road' in x):
            return '#7CFC00'
        elif ('lane' in x):
            return '#91c8ff'
        elif ('avenue' in x):
            return '#3c9c69'
        elif ('walk' in x):
            return '#ffa000'
        elif ('sqaure' in x):
            return '#004aff'
        elif ('drive' in x):
            return '#ef00ff'
        elif ('way' in x):
            return '#ffd800'
        else:
            return 'black'

    G = ox.graph_from_place(borough_name, network_type='all')

    # For the colouring, we take the attributes from each edge found extract the road name, and use the function above to create the colour array
    edge_attributes = ox.graph_to_gdfs(G, nodes=False)
    ec = [colourcode(str(row['name']).lower()) for index, row in edge_attributes.iterrows()]

    # We can finally draw the plot
    fig, ax = ox.plot_graph(G, bgcolor='white', axis_off=True, node_size=0, node_color='w', node_edgecolor='gray',
                            node_zorder=2,
                            edge_color=ec, edge_linewidth=0.5, edge_alpha=1, fig_height=20, save=True, dpi=1000);

draw_colourcoded_map()

'''
test codes
'''
# # gdf = ox.gdf_from_places(['United Kingdom', 'Ireland'])
# # gdf = ox.project_gdf(gdf)
# # fig, ax = ox.plot_shape(gdf)
# # remove nan from column
# incoms = [incom for incom in edge_attributes['name'] if str(incom) != 'nan']
# print(type(incoms))