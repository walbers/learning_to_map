# Sources
# http://ncdrisc.org/data-downloads-height.html
# https://hub.arcgis.com/datasets/a21fdb46d23e4ef896f31475217cbb08_1?geometry=-132.187%2C-88.331%2C227.812%2C88.537
import math
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
matplotlib.use('Agg')

men = False
color = 'RdPu'

map_df = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

x = map_df.plot()
# x.figure.savefig('fig1')

df = pd.read_csv('data/mean_height_18_countries.csv', header=0)
df = df[['Country', 'ISO', 'Sex', 'Year of birth', 'Mean height (cm)']]

# get data for men and women
df_men = df[df.Sex == 'Men']
df_women = df[df.Sex == 'Women']

# get rid of all years but 1996 (most recent year in data set)
df_men = df_men[df_men['Year of birth'] == 1996]
df_women = df_women[df_women['Year of birth'] == 1996]

data_for_map_men = df_men.rename(index=str, columns={'Year of birth': 'year', 'Mean height (cm)': 'height'})
data_for_map_women = df_women.rename(index=str, columns={'Year of birth': 'year', 'Mean height (cm)': 'height'})

print(data_for_map_men)
print(data_for_map_women)

if (men):
    merged_men = map_df.set_index('iso_a3').join(data_for_map_men.set_index('ISO'))
else:
    merged_women = map_df.set_index('iso_a3').join(data_for_map_women.set_index('ISO'))

mapping = 'height'

vmin, vmax = 130, 200
fig, ax = plt.subplots(1, figsize=(10, 6))

if (men):
    men_map = merged_men.plot(column=mapping, cmap=color, linewidth=.8, ax=ax, edgecolor='.8')
    men_map.figure.savefig('fig2')
else:
    women_map = merged_women.plot(column=mapping, cmap=color, linewidth=.8, ax=ax, edgecolor='.8')
    women_map.figure.savefig('fig2')


ax.axis('off')
if (men):
    ax.set_title('Height (cm) of men in 1996')
else:
    ax.set_title('Height (cm) of women in 1996')

sm = plt.cm.ScalarMappable(cmap=color, norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
cbar = fig.colorbar(sm)
if (men):
    fig.savefig('men_map.png',dpi=300)
else:
    fig.savefig('women_map.png',dpi=300)
