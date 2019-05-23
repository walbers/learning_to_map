# maps
import geopandas as gpd
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
matplotlib.use('Agg')

# the file
file = 'data/statistical-gis-boundaries-london/ESRI/London_Borough_Excluding_MHW.shp'

# gets a dataframe - the base map
map_df = gpd.read_file(file)

# info about data frame - the base map
print(map_df.head())
x = map_df.plot()
x.figure.savefig('fig1')


# gets a dataframe - data relevant to the base map
df = pd.read_csv('london-borough-profiles.csv', header=0)
print(df.head())

# get only these columns from the data file
df = df[['Area_name','Happiness_score_2011-14_(out_of_10)', 'Anxiety_score_2011-14_(out_of_10)',
'Population_density_(per_hectare)_2017',
'Mortality_rate_from_causes_considered_preventable_2012/14']]

# rename columns so they look better
data_for_map = df.rename(index=str, columns={'Happiness_score_2011-14_(out_of_10)': 'happiness',
'Anxiety_score_2011-14_(out_of_10)': 'anxiety',
'Population_density_(per_hectare)_2017': 'pop_density_per_hectare',
'Mortality_rate_from_causes_considered_preventable_2012/14': 'mortality'})
print(data_for_map.head())


# merge the two data frames
merged = map_df.set_index('NAME').join(data_for_map.set_index('Area_name'))
print(merged.head())

#  varible for the particular data
mapping = 'happiness'
# variables for the range
vmin, vmax = 120,220
# create figure and axes for matplotlib ??
fig, ax = plt.subplots(1, figsize=(10,6))

# plot the merged
x = merged.plot(column=mapping, cmap='Blues', linewidth=.8, ax=ax, edgecolor='.8')
x.figure.savefig('fig2')

# get rid off axises
ax.axis('off')
# sets title
ax.set_title("Populator Density per Hectare in London")
# sets annotation (data source) - location, color, size
ax.annotate('Source: me', xy=(.1, .08), xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=10)

# create colorbar as a legend
sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
cbar = fig.colorbar(sm)

# saving the final combined map with legend and title and annotation
fig.savefig('map_export.png', dpi=300)
