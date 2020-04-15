import csv
import plotly.express as px
import plotly.graph_objects as go

long_list = []
lat_list = []
label = []
boroughs = []
with open('Pubs.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader, None)
    for row in reader:
        long_list.append((row[10]))
        lat_list.append((row[11]))
        label.append(row[0])
        boroughs.append((row[4]))

mapbox_access_token = 'pk.eyJ1Ijoibmljb2xlbGVtYW4iLCJhIjoiY2s3cXJoeWRzMDVweTNvcXBoZHlkdWxnbCJ9.v5ZpKMG5A1_i8svZ03aSvg'
fig = go.Figure(go.Scattermapbox(lat=lat_list, lon=long_list, mode='markers',
        marker=go.scattermapbox.Marker(size=7), text=label,))

fig.update_layout(title='Location of pubs in Central London', autosize=True, hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(lat=51.514,
            lon=-0.093),
        pitch=0,
        zoom=14
    ),
)

fig.show()

from folium import plugins

# # let's start again with a clean copy of the map of San Francisco
# sanfran_map = folium.Map(location = [latitude, longitude], zoom_start = 12)
#
# # instantiate a mark cluster object for the incidents in the dataframe
# incidents = plugins.MarkerCluster().add_to(sanfran_map)
#
# # loop through the dataframe and add each data point to the mark cluster
# for lat, lng, label, in zip(df_incidents.Y, df_incidents.X, df_incidents.Category):
#     folium.Marker(
#         location=[lat, lng],
#         icon=None,
#         popup=label,
#     ).add_to(incidents)
#
# # display map
# sanfran_map
