import osmnx as ox

munich = ox.geocode_to_gdf("Munich, Germany")
ax = ox.project_gdf(munich).plot()
_ = ax.axis("off")