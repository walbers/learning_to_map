# Sources
# http://ncdrisc.org/data-downloads-height.html
# https://hub.arcgis.com/datasets/a21fdb46d23e4ef896f31475217cbb08_1?geometry=-132.187%2C-88.331%2C227.812%2C88.537

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
matplotlib.use('Agg')

file = 'data/world_map/Countries_WGS84.shp'
map_df = gpd.read_file(file)

print(map_df.head())
x = map_df.plot()
x.figure.savefig('fig1')


df = pd.read_csv('data/mean_height_18_countries.csv', header=0)
print(df.head())


df = df[['Country', 'Sex', 'Mean height (cm)']]
data_for_map = df.rename(index=str, columns={'Mean height (cm)': 'height'})

## !! PULL OUT ROWS HERE !!


print(data_for_map.head())

#merged = map_df.set_index('CNTRY_NAME').join(data_for_map.set_index('Country'))
#print(merged.head())

#mapping = 'height'

'''
vmin, vmax = 50, 250
fig, ax = plt.subplots(1, figsize(10, 6))

x= merged.plot(column = mapping, cmap='Blues', linewidth=.8, ax=ax, edgecolor=',8')
x.figure.savefig('fig2')

ax.axis('off')
ax.set_title('Height (cm) in world')

sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
cbar = fig.colorbar(sm)

fig.savefig('map.png',dpi=300)
'''

