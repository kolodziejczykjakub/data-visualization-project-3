import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

# ----------------------------- READ DATA -----------------------------------
data = pd.read_csv('./data/covid.csv')
data = data[data["date"] == "2020-06-15"]
data["NAME"] = data["Country/Region"]

try:
    europe = gpd.read_file("./data/Europe.shp")
except ValueError as e:
    print(e)

# -------------------------- PREPROCESS DATA --------------------------------
europe = europe.drop(["ORGN_NAME"], axis=1)
europe["area"] = europe["geometry"].area
europe = europe.merge(data, on='NAME', how="left")
europe = europe.dropna()

# ------------------------------ PLOTS ---------------------------------------
# 6
_, ax = plt.subplots(1, figsize=(10, 6))
europe.plot(ax=ax,
            column='confirmed',
            cmap='Greens',
            legend=True,
            legend_kwds={'label': "Confirmed covid cases",
                         'orientation': "horizontal"},
            linewidth=0.5,
            edgecolor='0.4',
            )
ax.axis('off')
plt.savefig('./figures/map_6.png', transparent=True)

# 5
_, ax = plt.subplots(1, figsize=(10, 6))
ax = europe.plot(ax=ax,
                 column='confirmed',
                 cmap='Greens',
                 legend=False,
                 linewidth=0.5,
                 edgecolor='0.4',
                 )
ax.axis('off')
plt.savefig('./figures/map_5.png', transparent=True)

# 4
_, ax = plt.subplots(1, figsize=(10, 6))
ax = europe.plot(ax=ax,
                 column='confirmed',
                 cmap='gray',
                 legend=True,
                 legend_kwds={'label': "Confirmed covid cases",
                              'orientation': "horizontal"},
                 linewidth=0.5,
                 edgecolor='0.4',
                 )
ax.axis('off')
plt.savefig('./figures/map_4.png', transparent=True)

# 3
_, ax = plt.subplots(1, figsize=(10, 6))
ax = europe.plot(ax=ax,
                 column='confirmed',
                 cmap='gray',
                 legend=False,
                 linewidth=0.5,
                 edgecolor='0.4',
                 )
ax.axis('off')
plt.savefig('./figures/map_3.png', transparent=True)

# 2
_, ax = plt.subplots(1, figsize=(10, 6))
ax = europe.plot(ax=ax,
                 column='confirmed',
                 cmap='twilight',
                 legend=True,
                 legend_kwds={'label': "Confirmed covid cases",
                              'orientation': "horizontal"},
                 linewidth=0.5,
                 edgecolor='0.4',
                 )
ax.axis('off')
plt.savefig('./figures/map_2.png', transparent=True)

# 1
_, ax = plt.subplots(1, figsize=(10, 6))
ax = europe.plot(ax=ax,
                 column='confirmed',
                 cmap='twilight',
                 legend=False,
                 linewidth=0.5,
                 edgecolor='0.4',
                 )
ax.axis('off')
plt.savefig('./figures/map_1.png', transparent=True)

