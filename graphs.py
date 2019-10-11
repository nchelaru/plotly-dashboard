import pandas as pd
import plotly.express as px
import numpy as np

## Create map
def sales_map():
    zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t' , encoding='latin-1')

    zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

    zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t' , encoding='latin-1')

    orders = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t' , encoding='latin-1')

    grouped = orders.groupby(['zipcode'])['city', 'state', 'totalprice'].agg('sum').reset_index()

    merged = pd.merge(grouped, zipcounty[['zipcode', 'latitude', 'longitude']], on='zipcode')

    merged.columns = ['zipcode', 'totalprice', 'Latitude', 'Longitude']

    merged = merged[merged['totalprice'] > 0]

    merged['log_totalprice'] = np.log(merged['totalprice'])

    px.set_mapbox_access_token("pk.eyJ1IjoibmQ4MjMiLCJhIjoiY2p1aDNheXltMHNuNTN6bng2Mjc0a2ZyOSJ9.aJwWqjS3PZcYKVckxisUNg")

    fig = px.scatter_mapbox(merged, lat="Latitude", lon="Longitude", size = "log_totalprice",
                            color = "log_totalprice",  color_continuous_scale=px.colors.diverging.RdYlGn[::-1],
                            zoom=2)

    return fig

