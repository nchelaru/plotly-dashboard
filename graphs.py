import pandas as pd
import plotly.express as px
import numpy as np
import plotly
from plotly import graph_objs as go
import datetime
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import math
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from chart_studio.plotly import plot, iplot
import plotly.figure_factory as ff
from datetime import datetime, timedelta
from functools import reduce


## Import data
zipcounty = pd.read_csv('https://github.com/nchelaru/plotly-dashboard/raw/master/zipcounty.txt', sep='\t' , encoding='latin-1')

zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

products = pd.read_csv('https://github.com/nchelaru/plotly-dashboard/raw/master/products.txt', sep='\t' , encoding='latin-1')

products['full_code'] = products['PRODUCTGROUPCODE'].astype(str) + '-' + products['PRODUCTID'].astype(str)

orders = pd.read_csv('https://github.com/nchelaru/plotly-dashboard/raw/master/orders.txt', sep='\t' , encoding='latin-1')

orders['orderyear'] = pd.to_datetime(orders['orderdate']).dt.year

orders = orders[orders['orderyear'] > 2009]

orderlines = pd.read_csv('https://github.com/nchelaru/plotly-dashboard/raw/master/orderlines.txt', sep='\t', encoding='latin-1')

orderlines['billyear'] = pd.to_datetime(orderlines['billdate']).dt.year

orderlines = orderlines[orderlines['billyear'] > 2009]

campaigns = pd.read_csv('https://github.com/nchelaru/plotly-dashboard/raw/master/campaigns.txt', sep='\t' , encoding='latin-1')

customers = pd.read_csv('https://github.com/nchelaru/plotly-dashboard/raw/master/customers.txt', sep='\t' , encoding='latin-1')



## Map
## data processing
# orders['orderyear'] = pd.to_datetime(orders['orderdate']).dt.year
#
# grouped = orders.groupby(['zipcode', 'orderdate'])['totalprice'].agg('sum')
#
# grouped1 = grouped.unstack().fillna(0).stack().reset_index()
#
# grouped1.columns = ['zipcode', 'orderdate', 'totalprice']
#
# grouped1 = grouped1.sample(n=600000, random_state=1)
#
# merged = pd.merge(grouped1, zipcounty[['zipcode', 'latitude', 'longitude']], on='zipcode')
#
# merged_2 = pd.merge(merged, orders[['zipcode', 'city', 'state']], on='zipcode', how='left')
#
# merged_3 = merged_2.drop_duplicates(subset=['orderdate', 'zipcode', 'latitude', 'longitude'], keep='first')
#
# merged_3['location'] = merged_3['zipcode'].astype(str) + '-' + merged_3['city'].astype(str) + ", " + merged_3['state'].astype('str')
#
#
# merged_3['log_totalprice'] = np.log(merged_3['totalprice'])
#
# merged_3 = merged_3.replace([np.inf, -np.inf], np.nan)
#
# merged_3 = merged_3.fillna(0)
#
# merged_3['orderyear'] = pd.to_datetime(merged_3['orderdate']).dt.year
#
# merged_3.columns = ['Zipcode', 'Date', 'TotalSpent', 'Latitude', 'Longitude', 'City', 'State', 'Location', 'Log10(TotalSpent)', 'Year']
#
# merged_3.to_csv('merged_3.csv', index=False)

def map_df():
    merged_3 = pd.read_csv('./map_data.csv')

    merged_3['Date'] = pd.to_datetime(merged_3['Date'])

    merged_3['Year'] = merged_3['Date'].dt.year

    merged_3['Date'] = merged_3['Date'].dt.date

    merged_3 = merged_3[['Date', 'Year', 'TotalSpent', 'Latitude', 'Longitude', 'Zipcode', 'Location', 'City', 'State']]

    merged_3.columns = ['OrderDate', 'Year', 'TotalRevenue', 'Latitude', 'Longitude', 'ZipCode', 'Location', 'City',
                        'State']

    merged_3['Log(TotalRevenue)'] = np.log(merged_3['TotalRevenue'])

    merged_3 = merged_3.replace([np.inf, -np.inf], np.nan)

    merged_3 = merged_3.fillna(0)

    df = merged_3.sort_values(by='OrderDate')

    return df


def map(df=map_df()):

    px.set_mapbox_access_token("pk.eyJ1IjoibmQ4MjMiLCJhIjoiY2p1aDNheXltMHNuNTN6bng2Mjc0a2ZyOSJ9.aJwWqjS3PZcYKVckxisUNg")

    fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size="Log(TotalRevenue)",
                            color = "Log(TotalRevenue)",  color_continuous_scale=px.colors.sequential.YlOrRd,
                            zoom=2, size_max=10, hover_name='Location', animation_frame='Year',
                            category_orders={'Year':[2010, 2011, 2012, 2013, 2014, 2015, 2016]})

    fig.update_layout(margin=dict(l=15, r=15, t=10, b=10),
                      autosize=True)

    return fig

# def sales_map():
#     orders['orderyear'] = pd.to_datetime(orders['orderdate']).dt.year
#
#     grouped = orders.groupby(['zipcode', 'orderyear'])['totalprice'].agg('sum')
#
#     grouped1 = grouped.unstack().fillna(0).stack().reset_index()
#
#     grouped1.columns = ['zipcode', 'orderyear', 'totalprice']
#
#     merged = pd.merge(grouped1, zipcounty[['zipcode', 'latitude', 'longitude']], on='zipcode')
#
#     merged_2 = pd.merge(merged, orders[['zipcode', 'city', 'state']], on='zipcode', how='left')
#
#     merged_3 = merged_2.drop_duplicates(subset=['orderyear', 'zipcode', 'latitude', 'longitude'], keep='first')
#
#     merged_3['location'] = merged_3['zipcode'].astype(str) + '-' + merged_3['city'].astype(str) + ", " + merged_3['state'].astype('str')
#
#     #merged_3 = merged_3[merged_3['totalprice'] > 0]
#
#     merged_3['log_totalprice'] = np.log(merged_3['totalprice'])
#
#     merged_3 = merged_3.replace([np.inf, -np.inf], np.nan)
#
#     merged_3 = merged_3.fillna(0)
#
#     merged_3.columns = ['Zipcode', 'Year', 'TotalSpent', 'Latitude', 'Longitude', 'City', 'State', 'Location', 'Log10(TotalSpent)']
#
#     merged_3['Year'] = merged_3['Year'].astype(int)
#
#     merged_3.sort_values(by='Year', inplace=True)
#
#     px.set_mapbox_access_token("pk.eyJ1IjoibmQ4MjMiLCJhIjoiY2p1aDNheXltMHNuNTN6bng2Mjc0a2ZyOSJ9.aJwWqjS3PZcYKVckxisUNg")
#
#     fig = px.scatter_mapbox(merged_3, lat="Latitude", lon="Longitude", size = "Log10(TotalSpent)",
#                             color = "Log10(TotalSpent)",  color_continuous_scale=px.colors.sequential.YlOrRd,
#                             zoom=2, size_max=10, hover_name='Location',
#                             animation_frame='Year', animation_group='Year',
#                             category_orders={'Year':[2010, 2011, 2012, 2013, 2014, 2015, 2016]})
#
#     fig.update_layout(margin=dict(l=30, r=30, t=20, b=20))
#
#     return fig


## Category+month heatmap
def cat_month_heatmap():
    merged = pd.merge(products[['PRODUCTID', 'PRODUCTGROUPNAME']],
                      orderlines[['productid', 'shipdate', 'totalprice']],
                      left_on='PRODUCTID', right_on='productid', how='inner')

    merged['shipdate-clean'] = pd.DatetimeIndex(merged['shipdate']).date

    x = merged.groupby(['shipdate-clean', 'PRODUCTGROUPNAME'])['totalprice'].agg('sum').reset_index()

    x= x[x['PRODUCTGROUPNAME'] != 'FREEBIE']

    x['shipdate-clean'] = pd.to_datetime(x['shipdate-clean'])

    fig = go.Figure(data=go.Heatmap(
        z=np.log(x['totalprice']),
        x=x['shipdate-clean'],
        y=x['PRODUCTGROUPNAME'],
        colorscale='Viridis'))

    fig.update_layout(margin=dict(l=30, r=30, t=20, b=20))

    return fig

## Stack area graph for campaigns
def stacked_area():
    merged = pd.merge(campaigns[['campaignid', 'channel']], orders[['orderdate', 'campaignid', 'totalprice']],
                      on='campaignid', how='inner')

    merged['ordermonth'] = pd.to_datetime(merged['orderdate']).dt.month

    merged['orderyear'] = pd.to_datetime(merged['orderdate']).dt.year

    x = merged.groupby(['ordermonth', 'orderyear', 'channel'])['totalprice'].agg('sum')

    b = x.unstack().fillna(0).stack().reset_index()

    b.columns = ['Month', 'Year', 'Channel', 'TotalRevenue']

    b = b.sort_values(by='Channel')

    fig = px.area(b, x="Month", y="TotalRevenue", color="Channel",
                  line_group="Channel", animation_frame='Year', range_y=[0, 700000],
                  category_orders={'Year':[2010, 2011, 2012, 2013, 2014, 2015, 2016]})

    #fig = fig.for_each_trace(lambda t: t.update(name=t.name.replace("channel=", "")))

    fig = fig.update_layout(showlegend=False,
                            margin=dict(l=30, r=30, t=20, b=20),
                            xaxis=go.layout.XAxis(
                                title=go.layout.xaxis.Title(
                                    text="Month"
                                )
                            ),
                            yaxis=go.layout.YAxis(
                                title=go.layout.yaxis.Title(
                                    text="Total revenue",
                                )
                            )
                            )

    return fig

## Parallel coordinate diagram
def para_df():
    merged_1 = pd.merge(orderlines[['shipdate', 'productid', 'orderid', 'totalprice']],
                        products[['PRODUCTID', 'PRODUCTGROUPNAME']],
                        left_on='productid', right_on='PRODUCTID',
                        how='inner')

    merged_2 = pd.merge(merged_1, orders[['campaignid', 'orderid']],
                        on='orderid', how='inner')

    merged_2['shipyear'] = pd.to_datetime(merged_2['shipdate']).dt.year

    merged_3 = pd.merge(merged_2, campaigns[['campaignid', 'freeshippingflag', 'channel']], on='campaignid',
                        how='inner')

    merged_3['log_totalprice'] = np.log(merged_3['totalprice'])

    merged_4 = merged_3.sample(n=1000, random_state=1)

    merged_4 = merged_4.sort_values(by='PRODUCTGROUPNAME')

    return merged_4

def para_coord(df=para_df()):
    fig = px.parallel_categories(df, dimensions=['freeshippingflag', 'PRODUCTGROUPNAME', 'channel'],
                                 color='log_totalprice',
                                 color_continuous_scale=px.colors.sequential.Inferno,
                                 labels={'PRODUCTGROUPNAME':'Product groupname',
                                         'freeshippingflag':'Free shipping',
                                         'channel':'Campaign channel'},
                                 height=500
                                 )

    fig = fig.update_layout(showlegend=False,
                      margin=dict(l=30, r=30, t=20, b=20)
                      )

    return fig


## Time-line
orders['orderdate'] = pd.DatetimeIndex(orders['orderdate']).date

x = orders.groupby(['orderdate'])['totalprice'].agg('sum').reset_index()

def sales_timeline(df=x):
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df['OrderDate'], y=df['TotalAmount'], name="Total sales",
                             line_color='lightgreen'))

    fig.update_layout(xaxis_rangeslider_visible=True,
                      margin=dict(l=30, r=30, t=10, b=20),
                      paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)')

    return fig


## Radar plot
def radat_plot():
    merged_1 = pd.merge(orders[['customerid', 'campaignid']], customers[['customerid', 'gender']], on='customerid',
                        how='inner')

    merged_2 = pd.merge(merged_1, campaigns[['campaignid', 'channel']], on='campaignid', how='inner')

    final = merged_2.groupby(['channel', 'gender'])['channel'].count().unstack().fillna(0)

    final['channel'] = final.index

    categories = final['channel']

    final['M'] = (final['M'] / final['M'].sum()) * 100

    final['F'] = (final['F'] / final['F'].sum()) * 100

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=final['F'],
        theta=categories,
        fill='toself',
        name='Female'
    ))
    fig.add_trace(go.Scatterpolar(
        r=final['M'],
        theta=categories,
        fill='toself',
        name='Male'
    ))

    return fig

## Campaign map
def calculate_initial_compass_bearing(pointA, pointB):
    """
    Calculates the bearing between two points.
    The formulae used is the following:
        θ = atan2(sin(Δlong).cos(lat2),
                  cos(lat1).sin(lat2) − sin(lat1).cos(lat2).cos(Δlong))
    :Parameters:
      - `pointA: The tuple representing the latitude/longitude for the
        first point. Latitude and longitude must be in decimal degrees
      - `pointB: The tuple representing the latitude/longitude for the
        second point. Latitude and longitude must be in decimal degrees
    :Returns:
      The bearing in degrees
    :Returns Type:
      float
    """
    if (type(pointA) != tuple) or (type(pointB) != tuple):
        raise TypeError("Only tuples are supported as arguments")

    lat1 = math.radians(pointA[0])
    lat2 = math.radians(pointB[0])

    diffLong = math.radians(pointB[1] - pointA[1])

    x = math.sin(diffLong) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
            * math.cos(lat2) * math.cos(diffLong))

    initial_bearing = math.atan2(x, y)

    # Now we have the initial bearing but math.atan2 return values
    # from -180° to + 180° which is not what we want for a compass bearing
    # The solution is to normalize the initial bearing as shown below
    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360

    return compass_bearing

def polar_plot():
    merged = pd.merge(orders[['zipcode']],
                      zipcounty[['zipcode', 'latitude', 'longitude']],
                      on='zipcode', how='inner')

    merged = merged.drop_duplicates(keep='first')

    bearings_list = []

    for i in list(zip(merged['latitude'], merged['longitude'])):
        ptA = (37.0902, -95.7129)
        bearings_list.append(calculate_initial_compass_bearing(ptA, i))

    merged['bearings'] = bearings_list

    merged['polar'] = pd.cut(merged['bearings'], 16, labels=['N', 'NNE', 'NE', 'ENE',
                                                             'E', 'ESE', 'SE', 'SSE',
                                                             'S', 'SSW', 'SW', 'WSW',
                                                             'W', 'WNW', 'NW', 'NNW'])

    orders['orderyear'] = pd.to_datetime(orders['orderdate']).dt.year

    merged_1 = pd.merge(orders[['orderyear', 'campaignid', 'zipcode', 'totalprice']],
                        campaigns[['campaignid', 'channel']],
                        on='campaignid', how='inner')

    merged_2 = pd.merge(merged_1, zipcounty[['zipcode', 'latitude', 'longitude']], on='zipcode')

    z = merged_1.groupby(['zipcode', 'channel', 'orderyear'])['totalprice'].mean()

    u = z.unstack().fillna(0).stack().reset_index()

    u.columns = ['zipcode', 'channel', 'orderyear', 'TotalSpent']

    #z = pd.DataFrame(z)

    #z = z.reset_index()

    final = pd.merge(u, merged[['zipcode', 'polar']], on='zipcode', how='inner')

    mean_final = final.groupby(['polar', 'channel', 'orderyear'])['TotalSpent'].mean()

    mean_final = mean_final.reset_index()

    mean_final = mean_final.sort_values(by=['orderyear', 'polar'])

    fig = px.bar_polar(mean_final, r="TotalSpent", theta="polar",
                       color="channel", animation_frame='orderyear',
                       color_discrete_sequence=px.colors.colorbrewer.Set3,
                       category_orders={'Year':[2010, 2011, 2012, 2013, 2014, 2015, 2016]})

    #fig = fig.for_each_trace(lambda t: t.update(name=t.name.replace("channel=", "")))

    fig = fig.update_layout(showlegend=False,
                            margin=dict(l=30, r=30, t=20, b=20))

    return fig

# def campaign_map():
#     orders['orderyear'] = pd.to_datetime(orders['orderdate']).dt.year
#
#     merged_1 = pd.merge(orders[['orderid', 'orderyear', 'campaignid', 'zipcode', 'totalprice']],
#                         campaigns[['campaignid', 'channel']],
#                         on='campaignid', how='inner')
#
#     merged_2 = pd.merge(merged_1, zipcounty[['zipcode', 'latitude', 'longitude']], on='zipcode')
#
#     z = merged_2.groupby(['zipcode', 'orderyear', 'channel'])['totalprice'].mean()
#
#     z = z.unstack(level=-1)
#
#     z.fillna(0, inplace=True)
#
#     z['Max_chnl_val'] = (z.max(axis=1) / z.sum(axis=1)) * 100
#
#     z['Max_chnl'] = z.drop('Max_chnl_val', axis=1, inplace=False).idxmax(axis=1)
#
#     z['zipcode'] = z.index
#
#     z.reset_index(drop=True, inplace=True)
#
#     z = z[~z['Max_chnl_val'].isnull()]
#
#     final = pd.merge(z[['zipcode', 'Max_chnl_val', 'Max_chnl']], zipcounty[['zipcode', 'latitude', 'longitude']],
#                      on='zipcode', how='left')
#
#     px.set_mapbox_access_token("pk.eyJ1IjoibmQ4MjMiLCJhIjoiY2p1aDNheXltMHNuNTN6bng2Mjc0a2ZyOSJ9.aJwWqjS3PZcYKVckxisUNg")
#
#     fig = px.scatter_mapbox(final, lat='latitude', lon='longitude',
#                             color='Max_chnl', size='Max_chnl_val',
#                             size_max=5, zoom=2)
#
#     fig = fig.for_each_trace(lambda t: t.update(name=t.name.replace("Max_chnl=", "")))
#
#     return fig


def scatter_df():
    orderlines = pd.read_csv('https://github.com/nchelaru/plotly-dashboard/raw/master/orderlines.txt', sep='\t', encoding='latin-1')

    orderlines['billyear'] = pd.to_datetime(orderlines['billdate']).dt.year

    orderlines = orderlines[orderlines['billyear'] > 2009]

    orderlines['billyear'] = orderlines['billyear'].astype(int)

    merged = pd.merge(orderlines, products[['PRODUCTID', 'PRODUCTGROUPNAME']],
                      left_on='productid', right_on='PRODUCTID', how='inner')

    merged = merged[~merged['PRODUCTGROUPNAME'].isnull()]

    merged = merged[merged['PRODUCTGROUPNAME'] != 'FREEBIE']

    return merged

def scatter_plot(df=scatter_df()):
    fig = px.scatter(df, x="unitprice", y="numunits",
                     size="totalprice", facet_row="PRODUCTGROUPNAME",
                     color='PRODUCTGROUPNAME', log_x=True, log_y=True,
                     category_orders={'PRODUCTGROUPNAME':['ARTWORK', 'APPAREL', 'BOOK', 'OTHER',
                                                  'CALENDAR', 'GAME', 'OCCASSION']},
                     height=900)

    fig = fig.update_layout(showlegend=False,
                            margin=dict(l=20, r=20, t=10, b=10))

    for a in fig.layout.annotations:
        a.text = a.text.split("=")[1]

    return fig


def assn_rules():
    # x = pd.merge(orderlines[['orderid', 'productid']], products[['PRODUCTID', 'PRODUCTGROUPNAME', 'full_code']],
    #              left_on='productid', right_on='PRODUCTID', how='inner')
    #
    # z = pd.merge(x, orders[['orderid', 'customerid']], on='orderid', how='inner')
    #
    # dataset = z.groupby(['customerid'])['full_code'].apply(list).values.tolist()
    #
    # new_list = []
    #
    # for i in dataset:
    #     if len(i) > 2:
    #         new_list.append(i)
    #
    # te = TransactionEncoder()
    # te_ary = te.fit(new_list).transform(new_list)
    # df = pd.DataFrame(te_ary, columns=te.columns_)
    # frequent_itemsets = apriori(df, min_support=0.003, use_colnames=True)
    #
    # rules = association_rules(frequent_itemsets, metric="confidence")
    #
    # rules["antecedents"] = rules["antecedents"].apply(lambda x: list(x)).astype("unicode")
    #
    # rules["consequents"] = rules["consequents"].apply(lambda x: list(x)).astype("unicode")
    #
    # rules.to_csv('rules.csv', index=False)

    rules = pd.read_csv('https://github.com/nchelaru/plotly-dashboard/raw/master/rules.csv')

    rules['antecedents'] == rules['antecedents'].astype(str)

    rules['antecedents'] = rules['antecedents'].replace('frozenset({', '')

    rules = rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']]

    rules.columns = ['Rule antecedents', 'Rule consequents', 'Support', 'Confidence', 'Lift']

    rules = rules.round(3)

    rules = rules.sort_values(by='Lift', ascending=False)

    return rules


## Gauge


def gauge_revenue():
    orders['orderdate'] = pd.to_datetime(orders['orderdate']).dt.date

    today = np.datetime64('2016-09-19')

    yesterday = np.datetime64('2016-09-18')

    today_revenue = orders[orders['orderdate'] == today]['totalprice'].sum()

    yesterday_revenue = orders[orders['orderdate'] == yesterday]['totalprice'].sum()

    fig = go.Figure(go.Indicator(
        title={"text": "Total revenue today"},
        mode="number+delta",
        value=today_revenue,
        number={'prefix': "$"},
        delta={'position': "top", 'reference': yesterday_revenue},
        domain={'x': [0, 1], 'y': [0, 1]}))

    fig.update_layout(
        margin=dict(l=30, r=30, t=30, b=10)
    )

    return fig


def gauge_orders():
    orders['orderdate'] = pd.to_datetime(orders['orderdate']).dt.date

    today = np.datetime64('2016-09-19')

    yesterday = np.datetime64('2016-09-18')

    today_orders = orders[orders['orderdate'] == today]['orderid'].count() + 3

    yesterday_orders = orders[orders['orderdate'] == yesterday]['orderid'].count()

    fig = go.Figure(go.Indicator(
        title={"text": "No. orders placed today"},
        mode="number+delta",
        value=today_orders,
        number={'suffix': " orders"},
        delta={'position': "top", 'reference': yesterday_orders},
        domain={'x': [0, 1], 'y': [0, 1]}))

    fig.update_layout(
        margin=dict(l=30, r=30, t=30, b=10)
    )

    return fig

def gauge_units():
    orders['orderdate'] = pd.to_datetime(orders['orderdate']).dt.date

    today = np.datetime64('2016-09-19')

    yesterday = np.datetime64('2016-09-18')

    today_numunits = orders[orders['orderdate'] == today]['numunits'].sum()

    yesterday_numunits = orders[orders['orderdate'] == yesterday]['numunits'].sum()

    fig = go.Figure(go.Indicator(
        title={"text": "No. units sold today"},
        mode="number+delta",
        value=today_numunits,
        number={'suffix': " units"},
        delta={'position': "top", 'reference': yesterday_numunits},
        domain={'x': [0, 1], 'y': [0, 1]}))

    fig.update_layout(
        margin=dict(l=30, r=30, t=30, b=10)
    )

    return fig


## Cards
def create_card(title, content, type):
    card = dbc.Card(
        dbc.CardBody(
            [
                html.H5(title, className="card-title"),
                html.Br(),
                html.H3(content, className="card-subtitle")
                ]
        ),
        color=type, inverse=True
    )
    return(card)

## Bullet chart
def bullet_chart():
    data = pd.read_json('https://cdn.rawgit.com/plotly/datasets/master/BulletData.json')

    measure_colors = ['rgb(63,102,153)', 'rgb(120,194,195)']
    range_colors = ['rgb(241,241,241)', 'rgb(245,225,218)']

    orderlines['billdate'] = pd.to_datetime(orderlines['billdate']).dt.date

    this_month = np.datetime64('2016-09-01')

    last_month = np.datetime64('2016-08-01')

    this_month_df = orderlines[(orderlines['billdate'] >= this_month) & (orderlines['billdate'] < np.datetime64('2016-09-19'))]

    this_month_df = pd.merge(this_month_df[['productid', 'billdate', 'totalprice']],
                          products[['PRODUCTID', 'PRODUCTGROUPNAME']],
                          left_on='productid', right_on='PRODUCTID', how='inner')

    this_month_grouped = this_month_df.groupby('PRODUCTGROUPNAME')['totalprice'].sum().reset_index()

    this_month_grouped.columns = ['productgroupname', 'this_month']

    last_month_df = orderlines[(orderlines['billdate'] >= last_month) & (orderlines['billdate'] < this_month)]

    last_month_df = pd.merge(last_month_df[['productid', 'billdate', 'totalprice']],
                          products[['PRODUCTID', 'PRODUCTGROUPNAME']],
                          left_on='productid', right_on='PRODUCTID', how='inner')

    last_month_grouped = last_month_df.groupby('PRODUCTGROUPNAME')['totalprice'].sum().reset_index()

    last_month_grouped.columns = ['productgroupname', 'last_month']


    last_yr_month = orderlines[(orderlines['billdate'] >= np.datetime64('2015-09-01')) & (orderlines['billdate'] <= np.datetime64('2015-09-30'))]

    last_yr_month_df = pd.merge(last_yr_month[['productid', 'billdate', 'totalprice']],
                             products[['PRODUCTID', 'PRODUCTGROUPNAME']],
                             left_on='productid', right_on='PRODUCTID', how='inner')

    last_yr_month_grouped = last_yr_month_df.groupby('PRODUCTGROUPNAME')['totalprice'].sum().reset_index()

    last_yr_month_grouped.columns = ['productgroupname', 'last_yr_month']

    df_list = [last_month_grouped, this_month_grouped, last_yr_month_grouped]

    bullet_df = reduce(lambda left,right: pd.merge(left, right, on='productgroupname'), df_list)

    bullet_df = bullet_df[bullet_df['productgroupname'] != 'FREEBIE']

    bullet_df['last_month'] = bullet_df['last_month'].astype(int)

    bullet_df['this_month'] = bullet_df['this_month'].astype(int)

    bullet_df['range'] = bullet_df['this_month'].apply(lambda x: [0, int(x)])

    bullet_df['measures'] = bullet_df['last_yr_month'].apply(lambda x: [0, int(x)])

    bullet_df['markers'] = bullet_df['last_month'].apply(lambda x: [int(x)])

    fig = ff.create_bullet(
        bullet_df, orientation='v',
        markers='markers',
        measures='range',
        ranges='measures',
        titles='productgroupname',
        range_colors=range_colors,
        measure_colors=measure_colors,
        title=None,
        width=None,
        height=None
    )

    fig.update_layout(showlegend=False,
                      margin=dict(l=20, r=30, t=20, b=20)
    )

    return fig

## Data table
operators = [['ge ', '>='],
             ['le ', '<='],
             ['lt ', '<'],
             ['gt ', '>'],
             ['ne ', '!='],
             ['eq ', '='],
             ['contains '],
             ['datestartswith ']]

def split_filter_part(filter_part):
    for operator_type in operators:
        for operator in operator_type:
            if operator in filter_part:
                name_part, value_part = filter_part.split(operator, 1)
                name = name_part[name_part.find('{') + 1: name_part.rfind('}')]

                value_part = value_part.strip()
                v0 = value_part[0]
                if (v0 == value_part[-1] and v0 in ("'", '"', '`')):
                    value = value_part[1: -1].replace('\\' + v0, v0)
                else:
                    try:
                        value = float(value_part)
                    except ValueError:
                        value = value_part

                # word operators need spaces after them in the filter string,
                # but we don't want these later
                return name, operator_type[0].strip(), value

    return [None] * 3

def orders_data():
    #df = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t' , encoding='latin-1')

    df = orders.drop(['zipcode', 'numorderlines', 'paymenttype', 'orderyear'], axis=1)

    df.columns = ['OrderID', 'CustomerID', 'CampaignID', 'OrderDate', 'City', 'State', 'TotalAmount', 'NumUnits']

    df['OrderDate'] = pd.to_datetime(df['OrderDate']).dt.date

    datelimit = np.datetime64('2016-09-01')

    df = df[df['OrderDate'] >= datelimit]

    df = df.fillna(" ")

    return df


def waterfall_chart():
    fig = go.Figure(go.Waterfall(
        name="20", orientation="v",
        measure=["relative", "relative", "total", "relative", "relative", "total"],
        x=["Sales", "Consulting", "Net revenue", "Purchases", "Other expenses", "Profit before tax"],
        textposition="outside",
        text=["+60", "+80", "", "-40", "-20", "Total"],
        y=[60, 80, 0, -40, -20, 0],
        connector={"line": {"color": "rgb(63, 63, 63)"}},
    ))

    fig.update_layout(
        margin=dict(l=30, r=30, t=10, b=10)
    )

    return fig