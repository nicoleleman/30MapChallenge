from urllib.request import urlopen
import json
import numpy as np
import pandas as pd
import plotly.express as px

with urlopen("https://martinjc.github.io/UK-GeoJSON/json/eng/topo_eer.json") as response:
    boroughs = json.load(response)

fig = px.choropleth(geojson=boroughs,
                    color_continuous_scale="Viridis",
                    range_color=(0, 12),
                    scope="europe"
                    )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

fig.show()