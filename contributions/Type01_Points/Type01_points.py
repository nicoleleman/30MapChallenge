import csv
import plotly.express as px
import plotly.graph_objects as go

long_list = []
lat_list = []
label = []
with open('Pubs.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader, None)
    for row in reader:
        long_list.append((row[10]))
        lat_list.append((row[11]))
        label.append(row[0])

mapbox_access_token = 'pk.eyJ1Ijoibmljb2xlbGVtYW4iLCJhIjoiY2s3cXJoeWRzMDVweTNvcXBoZHlkdWxnbCJ9.v5ZpKMG5A1_i8svZ03aSvg'
fig = go.Figure(go.Scattermapbox(lat=lat_list, lon=long_list, mode='markers',
        marker=go.scattermapbox.Marker(size=5), text=label,))

fig.update_layout(title='Location of pubs in Central London', autosize=True, hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(lat=51.5,
            lon=-0.12),
        pitch=0,
        zoom=10
    ),
)

fig.show()

