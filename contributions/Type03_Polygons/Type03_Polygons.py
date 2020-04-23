from urllib.request import urlopen
import json
import numpy as np
import pandas as pd
import plotly.express as px

with open('Counties_and_Unitary_Authorities_December_2016_Full_Extent_Boundaries_in_England_and_Wales.geojson') as response:
    counties = json.load(response)

df = pd.read_csv("Average-prices-2020-02.csv", dtype={"Area_Code": str})
data = df[['Area_Code','Average_Price']]

fig = px.choropleth_mapbox(data, geojson=counties,
                    locations = 'Area_Code',
                    color = 'Average_Price',
                    color_continuous_scale="Viridis",
                    range_color=(0, 1500000),
                    mapbox_style="carto-positron",
                    zoom = 5,
                    center={"lat": 53.1105, "lon": -1.1380},
                    labels={'Average_Price': 'Average Housing Price (£)'}
                    )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

