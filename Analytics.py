
import pandas as pd
import folium
from folium.plugins import HeatMap
import branca.colormap as cm 
import requests 
# 1 definir el endpoint 
url = 'https://data.lacity.org/resource/2nrs-mtv8.json'

params = {
    "$limit": 50,
    }

response  = requests.get(url, params)

print(response)

data = response.json()
df = pd.DataFrame(data)


df ['lat'] = pd.to_numeric(df['LAT'], errors= 'coerce')
df ['lon'] = pd.to_numeric(df['LON'], errors= 'coerce')
 
df_clean = df.dropna(subset=['LAT', 'LON']).copy()


map_center = [df_clean['LAT'].mean(), df_clean['LON'].mean()]

m = folium.Map(location=map_center, zoom_start=11, tiles='OpenStreetMap')

heat_data = df_clean[['LAT', 'LON']].values.tolist()

HeatMap(heat_data).add_to(m)

m.save("LAPD_crime_heatmap_with_legend.html")

m


