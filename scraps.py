z['Max_chnl_val'] = z.max(axis=0) / z.sum(axis=0)

z['Max_chnl'] = z.idxmax(axis=1)

z.max(axis=0)
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t', encoding='latin-1')

zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t', encoding='latin-1')

products = pd.read_csv('/Users/nancy/Downloads/products.txt', sep='\t', encoding='latin-1')

orders = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t', encoding='latin-1')

orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')

campaigns = pd.read_csv('/Users/nancy/Downloads/campaigns.txt', sep='\t', encoding='latin-1')

customers = pd.read_csv('/Users/nancy/Downloads/customers.txt', sep='\t', encoding='latin-1')

merged_1 = pd.merge(orders[['orderid', 'campaignid', 'zipcode', 'totalprice']], campaigns[['campaignid', 'channel']],
                    on='campaignid', how='inner')

merged_2 = pd.merge(merged_1, zipcounty[['zipcode', 'latitude', 'longitude']], on='zipcode')

z = merged_2.groupby(['zipcode', 'channel'])['totalprice'].mean()

z = z.unstack(level=-1)

z.fillna(0, inplace=True)

z['Max_chnl_val'] = z.max(axis=1) / z.sum(axis=1)

z['Max_chnl'] = z.idxmax(axis=1)

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t', encoding='latin-1')

zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t', encoding='latin-1')

products = pd.read_csv('/Users/nancy/Downloads/products.txt', sep='\t', encoding='latin-1')

orders = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t', encoding='latin-1')

orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')

campaigns = pd.read_csv('/Users/nancy/Downloads/campaigns.txt', sep='\t', encoding='latin-1')

customers = pd.read_csv('/Users/nancy/Downloads/customers.txt', sep='\t', encoding='latin-1')

merged_1 = pd.merge(orders[['orderid', 'campaignid', 'zipcode', 'totalprice']], campaigns[['campaignid', 'channel']],
                    on='campaignid', how='inner')

merged_2 = pd.merge(merged_1, zipcounty[['zipcode', 'latitude', 'longitude']], on='zipcode')

z = merged_2.groupby(['zipcode', 'channel'])['totalprice'].mean()

z = z.unstack(level=-1)

z.fillna(0, inplace=True)

z['Max_chnl_val'] = (z.max(axis=1) / z.sum(axis=1)) * 100

z['Max_chnl'] = z.idxmax(axis=1)

z['zipcode'] = z.index

z.reset_index(drop=True, inplace=True)

final = pd.merge(z, zipcounty[['zipcode', 'latitude', 'longitude']], on='zipcode', how='left')

px.set_mapbox_access_token("pk.eyJ1IjoibmQ4MjMiLCJhIjoiY2p1aDNheXltMHNuNTN6bng2Mjc0a2ZyOSJ9.aJwWqjS3PZcYKVckxisUNg")

fig = px.scatter_mapbox(final, lat='latitude', lon='longitude', color='Max_chnl', size='Max_chnl_val')

st.write(fig)

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t', encoding='latin-1')

zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t', encoding='latin-1')

products = pd.read_csv('/Users/nancy/Downloads/products.txt', sep='\t', encoding='latin-1')

orders = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t', encoding='latin-1')

orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')

campaigns = pd.read_csv('/Users/nancy/Downloads/campaigns.txt', sep='\t', encoding='latin-1')

customers = pd.read_csv('/Users/nancy/Downloads/customers.txt', sep='\t', encoding='latin-1')

merged_1 = pd.merge(orders[['orderid', 'campaignid', 'zipcode', 'totalprice']], campaigns[['campaignid', 'channel']],
                    on='campaignid', how='inner')

merged_2 = pd.merge(merged_1, zipcounty[['zipcode', 'latitude', 'longitude']], on='zipcode')

z = merged_2.groupby(['zipcode', 'channel'])['totalprice'].mean()

z = z.unstack(level=-1)

z.fillna(0, inplace=True)

z['Max_chnl_val'] = (z.max(axis=1) / z.sum(axis=1)) * 100

z['Max_chnl'] = z.idxmax(axis=1)

z['zipcode'] = z.index

z.reset_index(drop=True, inplace=True)

final = pd.merge(z[['zipcode', 'Max_chnl_val', 'Max_chnl']], zipcounty[['zipcode', 'latitude', 'longitude']],
                 on='zipcode', how='left')

final.info()
px.set_mapbox_access_token("pk.eyJ1IjoibmQ4MjMiLCJhIjoiY2p1aDNheXltMHNuNTN6bng2Mjc0a2ZyOSJ9.aJwWqjS3PZcYKVckxisUNg")

fig = px.scatter_mapbox(final, lat='latitude', lon='longitude', color='Max_chnl', size='Max_chnl_val')

final.head()

final['Max_chnl_val'].head()
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t', encoding='latin-1')

zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t', encoding='latin-1')

products = pd.read_csv('/Users/nancy/Downloads/products.txt', sep='\t', encoding='latin-1')

orders = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t', encoding='latin-1')

orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')

campaigns = pd.read_csv('/Users/nancy/Downloads/campaigns.txt', sep='\t', encoding='latin-1')

customers = pd.read_csv('/Users/nancy/Downloads/customers.txt', sep='\t', encoding='latin-1')

merged_1 = pd.merge(orders[['orderid', 'campaignid', 'zipcode', 'totalprice']], campaigns[['campaignid', 'channel']],
                    on='campaignid', how='inner')

merged_2 = pd.merge(merged_1, zipcounty[['zipcode', 'latitude', 'longitude']], on='zipcode')

z = merged_2.groupby(['zipcode', 'channel'])['totalprice'].mean()

z = z.unstack(level=-1)

z.fillna(0, inplace=True)

z['Max_chnl_val'] = (z.max(axis=1) / z.sum(axis=1)) * 100

z['Max_chnl'] = z.drop(['Max_chnl_val']).idxmax(axis=1)

z['zipcode'] = z.index

z.reset_index(drop=True, inplace=True)

final = pd.merge(z[['zipcode', 'Max_chnl_val', 'Max_chnl']], zipcounty[['zipcode', 'latitude', 'longitude']],
                 on='zipcode', how='left')

px.set_mapbox_access_token("pk.eyJ1IjoibmQ4MjMiLCJhIjoiY2p1aDNheXltMHNuNTN6bng2Mjc0a2ZyOSJ9.aJwWqjS3PZcYKVckxisUNg")

fig = px.scatter_mapbox(final, lat='latitude', lon='longitude', color='Max_chnl')

st.write(fig)

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t', encoding='latin-1')

zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t', encoding='latin-1')

products = pd.read_csv('/Users/nancy/Downloads/products.txt', sep='\t', encoding='latin-1')

orders = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t', encoding='latin-1')

orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')

campaigns = pd.read_csv('/Users/nancy/Downloads/campaigns.txt', sep='\t', encoding='latin-1')

customers = pd.read_csv('/Users/nancy/Downloads/customers.txt', sep='\t', encoding='latin-1')

merged_1 = pd.merge(orders[['orderid', 'campaignid', 'zipcode', 'totalprice']], campaigns[['campaignid', 'channel']],
                    on='campaignid', how='inner')

merged_2 = pd.merge(merged_1, zipcounty[['zipcode', 'latitude', 'longitude']], on='zipcode')

z = merged_2.groupby(['zipcode', 'channel'])['totalprice'].mean()

z = z.unstack(level=-1)

z.fillna(0, inplace=True)

z['Max_chnl_val'] = (z.max(axis=1) / z.sum(axis=1)) * 100

z['Max_chnl'] = z[-1].idxmax(axis=1)

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t', encoding='latin-1')

zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t', encoding='latin-1')

products = pd.read_csv('/Users/nancy/Downloads/products.txt', sep='\t', encoding='latin-1')

orders = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t', encoding='latin-1')

orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')

campaigns = pd.read_csv('/Users/nancy/Downloads/campaigns.txt', sep='\t', encoding='latin-1')

customers = pd.read_csv('/Users/nancy/Downloads/customers.txt', sep='\t', encoding='latin-1')

merged_1 = pd.merge(orders[['orderid', 'campaignid', 'zipcode', 'totalprice']], campaigns[['campaignid', 'channel']],
                    on='campaignid', how='inner')

merged_2 = pd.merge(merged_1, zipcounty[['zipcode', 'latitude', 'longitude']], on='zipcode')

z = merged_2.groupby(['zipcode', 'channel'])['totalprice'].mean()

z = z.unstack(level=-1)

z.fillna(0, inplace=True)

z['Max_chnl_val'] = (z.max(axis=1) / z.sum(axis=1)) * 100

z['Max_chnl'] = z.drop(['Max_chnl_val'], inplace=False).idxmax(axis=1)

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t', encoding='latin-1')

zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t', encoding='latin-1')

products = pd.read_csv('/Users/nancy/Downloads/products.txt', sep='\t', encoding='latin-1')

orders = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t', encoding='latin-1')

orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')

campaigns = pd.read_csv('/Users/nancy/Downloads/campaigns.txt', sep='\t', encoding='latin-1')

customers = pd.read_csv('/Users/nancy/Downloads/customers.txt', sep='\t', encoding='latin-1')

merged_1 = pd.merge(orders[['orderid', 'campaignid', 'zipcode', 'totalprice']], campaigns[['campaignid', 'channel']],
                    on='campaignid', how='inner')

merged_2 = pd.merge(merged_1, zipcounty[['zipcode', 'latitude', 'longitude']], on='zipcode')

z = merged_2.groupby(['zipcode', 'channel'])['totalprice'].mean()

z = z.unstack(level=-1)

z.fillna(0, inplace=True)

z['Max_chnl_val'] = (z.max(axis=1) / z.sum(axis=1)) * 100

z['Max_chnl'] = z.drop('Max_chnl_val', inplace=False).idxmax(axis=1)

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t', encoding='latin-1')

zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t', encoding='latin-1')

products = pd.read_csv('/Users/nancy/Downloads/products.txt', sep='\t', encoding='latin-1')

orders = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t', encoding='latin-1')

orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')

campaigns = pd.read_csv('/Users/nancy/Downloads/campaigns.txt', sep='\t', encoding='latin-1')

customers = pd.read_csv('/Users/nancy/Downloads/customers.txt', sep='\t', encoding='latin-1')

merged_1 = pd.merge(orders[['orderid', 'campaignid', 'zipcode', 'totalprice']], campaigns[['campaignid', 'channel']],
                    on='campaignid', how='inner')

merged_2 = pd.merge(merged_1, zipcounty[['zipcode', 'latitude', 'longitude']], on='zipcode')

z = merged_2.groupby(['zipcode', 'channel'])['totalprice'].mean()

z = z.unstack(level=-1)

z.fillna(0, inplace=True)

z['Max_chnl_val'] = (z.max(axis=1) / z.sum(axis=1)) * 100

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t', encoding='latin-1')

zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t', encoding='latin-1')

products = pd.read_csv('/Users/nancy/Downloads/products.txt', sep='\t', encoding='latin-1')

orders = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t', encoding='latin-1')

orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')

campaigns = pd.read_csv('/Users/nancy/Downloads/campaigns.txt', sep='\t', encoding='latin-1')

customers = pd.read_csv('/Users/nancy/Downloads/customers.txt', sep='\t', encoding='latin-1')

merged_1 = pd.merge(orders[['orderid', 'campaignid', 'zipcode', 'totalprice']], campaigns[['campaignid', 'channel']],
                    on='campaignid', how='inner')

merged_2 = pd.merge(merged_1, zipcounty[['zipcode', 'latitude', 'longitude']], on='zipcode')

z = merged_2.groupby(['zipcode', 'channel'])['totalprice'].mean()

z = z.unstack(level=-1)

z.fillna(0, inplace=True)

z['Max_chnl_val'] = (z.max(axis=1) / z.sum(axis=1)) * 100

z['Max_chnl'] = z.drop('Max_chnl_val', axis=1, inplace=False).idxmax(axis=1)

z['zipcode'] = z.index

z.reset_index(drop=True, inplace=True)

final = pd.merge(z[['zipcode', 'Max_chnl_val', 'Max_chnl']], zipcounty[['zipcode', 'latitude', 'longitude']],
                 on='zipcode', how='left')

px.set_mapbox_access_token("pk.eyJ1IjoibmQ4MjMiLCJhIjoiY2p1aDNheXltMHNuNTN6bng2Mjc0a2ZyOSJ9.aJwWqjS3PZcYKVckxisUNg")

fig = px.scatter_mapbox(final, lat='latitude', lon='longitude', color='Max_chnl')

fig = px.scatter_mapbox(final, lat='latitude', lon='longitude', color='Max_chnl', size='Max_chnl_val')

carshare = px.data.carshare()
carshare.head()
final[final['Max_chnl_var'.isnull()]]
final[final['Max_chnl_var'].isnull()]
final[final['Max_chnl_val'].isnull()]
z[z['Max_chnl_val'].isnull()]
test = z[z['Max_chnl_val'].isnull()]
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t', encoding='latin-1')

zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t', encoding='latin-1')

products = pd.read_csv('/Users/nancy/Downloads/products.txt', sep='\t', encoding='latin-1')

orders = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t', encoding='latin-1')

orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')

campaigns = pd.read_csv('/Users/nancy/Downloads/campaigns.txt', sep='\t', encoding='latin-1')

customers = pd.read_csv('/Users/nancy/Downloads/customers.txt', sep='\t', encoding='latin-1')

merged_1 = pd.merge(orders[['orderid', 'campaignid', 'zipcode', 'totalprice']], campaigns[['campaignid', 'channel']],
                    on='campaignid', how='inner')

merged_2 = pd.merge(merged_1, zipcounty[['zipcode', 'latitude', 'longitude']], on='zipcode')

z = merged_2.groupby(['zipcode', 'channel'])['totalprice'].mean()

z = z.unstack(level=-1)

z.fillna(0, inplace=True)

z['Max_chnl_val'] = (z.max(axis=1) / z.sum(axis=1)) * 100

z['Max_chnl'] = z.drop('Max_chnl_val', axis=1, inplace=False).idxmax(axis=1)

z['zipcode'] = z.index

z.reset_index(drop=True, inplace=True)

z = z[~z['Max_chnl_val'].isnull()]

final = pd.merge(z[['zipcode', 'Max_chnl_val', 'Max_chnl']], zipcounty[['zipcode', 'latitude', 'longitude']],
                 on='zipcode', how='left')

px.set_mapbox_access_token("pk.eyJ1IjoibmQ4MjMiLCJhIjoiY2p1aDNheXltMHNuNTN6bng2Mjc0a2ZyOSJ9.aJwWqjS3PZcYKVckxisUNg")

fig = px.scatter_mapbox(final, lat='latitude', lon='longitude', color='Max_chnl', size='Max_chnl_val')

st.write(fig)

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t', encoding='latin-1')

zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t', encoding='latin-1')

products = pd.read_csv('/Users/nancy/Downloads/products.txt', sep='\t', encoding='latin-1')

orders = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t', encoding='latin-1')

orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')

campaigns = pd.read_csv('/Users/nancy/Downloads/campaigns.txt', sep='\t', encoding='latin-1')

customers = pd.read_csv('/Users/nancy/Downloads/customers.txt', sep='\t', encoding='latin-1')

merged = pd.merge(orderlines[['productid', 'totalprice']], products[['PRODUCTID', 'PRODUCTGROUPNAME']],
                  left_on='productid', right_on='PRODUCTID', how='inner')

merged.info()
merged[merged['PRODUCTGROUPNAME'].isnull()]
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t', encoding='latin-1')

zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t', encoding='latin-1')

products = pd.read_csv('/Users/nancy/Downloads/products.txt', sep='\t', encoding='latin-1')

orders = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t', encoding='latin-1')

orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')

campaigns = pd.read_csv('/Users/nancy/Downloads/campaigns.txt', sep='\t', encoding='latin-1')

customers = pd.read_csv('/Users/nancy/Downloads/customers.txt', sep='\t', encoding='latin-1')

customers.info()
orderlines.info()
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t', encoding='latin-1')

zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t', encoding='latin-1')

products = pd.read_csv('/Users/nancy/Downloads/products.txt', sep='\t', encoding='latin-1')

orders = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t', encoding='latin-1')

orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')

campaigns = pd.read_csv('/Users/nancy/Downloads/campaigns.txt', sep='\t', encoding='latin-1')

customers = pd.read_csv('/Users/nancy/Downloads/customers.txt', sep='\t', encoding='latin-1')

products['full_code'] = products['PRODUCTGROUPCODE'].astype(str) + '-' + products['PRODUCTID']
products['full_code'] = products['PRODUCTGROUPCODE'].astype(str) + '-' + products['PRODUCTID'].astype(str)
x = pd.merge(orderlines[['orderid', 'productid']], products[['PRODUCTID', 'PRODUCTGROUPNAME', 'full_code']], )
x = pd.merge(orderlines[['orderid', 'productid']], products[['PRODUCTID', 'PRODUCTGROUPNAME', 'full_code']], \)
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t', encoding='latin-1')

zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t', encoding='latin-1')

products = pd.read_csv('/Users/nancy/Downloads/products.txt', sep='\t', encoding='latin-1')

products['full_code'] = products['PRODUCTGROUPCODE'].astype(str) + '-' + products['PRODUCTID'].astype(str)

orders = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t', encoding='latin-1')

orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')

campaigns = pd.read_csv('/Users/nancy/Downloads/campaigns.txt', sep='\t', encoding='latin-1')

customers = pd.read_csv('/Users/nancy/Downloads/customers.txt', sep='\t', encoding='latin-1')

x = pd.merge(orderlines[['orderid', 'productid']], products[['PRODUCTID', 'PRODUCTGROUPNAME', 'full_code']],
             left_on='productid', right_on='PRODUCTID', how='inner')
z = pd.merge(x, orders[['orderid', 'customerid']], on='orderid', how='inner')
v = pd.crosstab(z['customerid'], z['full_code'])
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t', encoding='latin-1')

zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t', encoding='latin-1')

products = pd.read_csv('/Users/nancy/Downloads/products.txt', sep='\t', encoding='latin-1')

products['full_code'] = products['PRODUCTGROUPCODE'].astype(str) + '-' + products['PRODUCTID'].astype(str)

orders = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t', encoding='latin-1')

orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')

campaigns = pd.read_csv('/Users/nancy/Downloads/campaigns.txt', sep='\t', encoding='latin-1')

customers = pd.read_csv('/Users/nancy/Downloads/customers.txt', sep='\t', encoding='latin-1')

x = pd.merge(orderlines[['orderid', 'productid']], products[['PRODUCTID', 'PRODUCTGROUPNAME', 'full_code']],
             left_on='productid', right_on='PRODUCTID', how='inner')

z = pd.merge(x, orders[['orderid', 'customerid']], on='orderid', how='inner')

e = z.groupby(['customerid'])['full_code'].apply(list).values.tolist()

len(e)
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t', encoding='latin-1')

zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t', encoding='latin-1')

products = pd.read_csv('/Users/nancy/Downloads/products.txt', sep='\t', encoding='latin-1')

products['full_code'] = products['PRODUCTGROUPCODE'].astype(str) + '-' + products['PRODUCTID'].astype(str)

orders = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t', encoding='latin-1')

orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')

campaigns = pd.read_csv('/Users/nancy/Downloads/campaigns.txt', sep='\t', encoding='latin-1')

customers = pd.read_csv('/Users/nancy/Downloads/customers.txt', sep='\t', encoding='latin-1')

x = pd.merge(orderlines[['orderid', 'productid']], products[['PRODUCTID', 'PRODUCTGROUPNAME', 'full_code']],
             left_on='productid', right_on='PRODUCTID', how='inner')

z = pd.merge(x, orders[['orderid', 'customerid']], on='orderid', how='inner')

e = z.groupby(['customerid'])['full_code'].apply(list).values.tolist()

print(len(e))
f = pd.DataFrame(e)
dataset = dataset[1:600]
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.9, use_colnames=True)

frequent_itemsets.head()

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
frequent_itemsets = apriori(df, min_support=0.9, use_colnames=True)
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)
dataset = z.groupby(['customerid'])['full_code'].apply(list).values.tolist()

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.7, use_colnames=True)

frequent_itemsets.head()

dataset = z.groupby(['orderid'])['full_code'].apply(list).values.tolist()
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)

frequent_itemsets.head()

dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)

frequent_itemsets

type(dataset)
dataset.head()
dataset[1:3]
dataset = z.groupby(['orderid'])['full_code'].apply(list).values.tolist()

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

# zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t' , encoding='latin-1')

# zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

# zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t' , encoding='latin-1')

products = pd.read_csv('/Users/nancy/Downloads/products.txt', sep='\t', encoding='latin-1')

products['full_code'] = products['PRODUCTGROUPCODE'].astype(str) + '-' + products['PRODUCTID'].astype(str)

orders = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t', encoding='latin-1')

orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')

# campaigns = pd.read_csv('/Users/nancy/Downloads/campaigns.txt', sep='\t' , encoding='latin-1')

customers = pd.read_csv('/Users/nancy/Downloads/customers.txt', sep='\t', encoding='latin-1')

x = pd.merge(orderlines[['orderid', 'productid']], products[['PRODUCTID', 'PRODUCTGROUPNAME', 'full_code']],
             left_on='productid', right_on='PRODUCTID', how='inner')

dataset = x.groupby(['orderid'])['full_code'].apply(list).values.tolist()
for i in dataset:
    if len(i) > 2:
        print(i)

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemset = apriori(df, min_support=0.6, use_colnames=True)

for i in dataset:
    if len(i) > 1:
        new_list.append()

new_list = []
for i in dataset:
    if len(i) > 1:
        new_list.append()

new_list = []
for i in dataset:
    if len(i) > 1:
        new_list.append(i)

te = TransactionEncoder()
te_ary = te.fit(new_list).transform(new_list)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemset = apriori(df, min_support=0.6, use_colnames=True)

te = TransactionEncoder()
te_ary = te.fit(new_list).transform(new_list)

df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemset = apriori(df, min_support=0.2, use_colnames=True)
dataset = x.groupby(['customerid'])['full_code'].apply(list).values.tolist()

new_list = []
for i in dataset:
    if len(i) > 1:
        new_list.append(i)

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

# zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t' , encoding='latin-1')

# zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

# zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t' , encoding='latin-1')

products = pd.read_csv('/Users/nancy/Downloads/products.txt', sep='\t', encoding='latin-1')

products['full_code'] = products['PRODUCTGROUPCODE'].astype(str) + '-' + products['PRODUCTID'].astype(str)

orders = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t', encoding='latin-1')

orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')

# campaigns = pd.read_csv('/Users/nancy/Downloads/campaigns.txt', sep='\t' , encoding='latin-1')

customers = pd.read_csv('/Users/nancy/Downloads/customers.txt', sep='\t', encoding='latin-1')

x = pd.merge(orderlines[['orderid', 'productid']], products[['PRODUCTID', 'PRODUCTGROUPNAME', 'full_code']],
             left_on='productid', right_on='PRODUCTID', how='inner')

z = pd.merge(x, orders[['orderid', 'customerid']], on='orderid', how='inner')

dataset = z.groupby(['customerid'])['full_code'].apply(list).values.tolist()

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.4, use_colnames=True)

dataset = z.groupby(['customerid'])['PRODUCTGROUPNAME'].apply(list).values.tolist()

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.4, use_colnames=True)

frequent_itemsets.head()

dataset = z.groupby(['orderid'])['full_code'].apply(list).values.tolist()

dataset = z.groupby(['orderid'])['full_code'].apply(list).values.tolist()

new_list = []

for i in new_list:
    if len(i) > 2:
        new_list.append(i)

te = TransactionEncoder()
te_ary = te.fit(new_list).transform(new_list)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.4, use_colnames=True)

frequent_itemsets
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

# zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t' , encoding='latin-1')

# zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

# zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t' , encoding='latin-1')

products = pd.read_csv('/Users/nancy/Downloads/products.txt', sep='\t', encoding='latin-1')

products['full_code'] = products['PRODUCTGROUPCODE'].astype(str) + '-' + products['PRODUCTID'].astype(str)

orders = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t', encoding='latin-1')

orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')

customers = pd.read_csv('/Users/nancy/Downloads/customers.txt', sep='\t', encoding='latin-1')

pd.crosstab(orderlines['orderlineid'], orderlines['orderid'])
pd.crosstab(orderlines['orderid'], orderlines['orderlineid'])
u = orderlines.groupby('orderid')['orderlineid']
u = orderlines.groupby('orderid')['orderlineid'].count()
u.tail()
u.columns
u.columns()
u.head()
g = pd.DataFrame(u)
g.head()
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

# zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t' , encoding='latin-1')

# zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

# zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t' , encoding='latin-1')

products = pd.read_csv('/Users/nancy/Downloads/products.txt', sep='\t', encoding='latin-1')

products['full_code'] = products['PRODUCTGROUPCODE'].astype(str) + '-' + products['PRODUCTID'].astype(str)

orders = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t', encoding='latin-1')

orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')

# campaigns = pd.read_csv('/Users/nancy/Downloads/campaigns.txt', sep='\t' , encoding='latin-1')

customers = pd.read_csv('/Users/nancy/Downloads/customers.txt', sep='\t', encoding='latin-1')

x = pd.merge(orderlines[['orderid', 'productid']], products[['PRODUCTID', 'PRODUCTGROUPNAME', 'full_code']],
             left_on='productid', right_on='PRODUCTID', how='inner')

z = pd.merge(x, orders[['orderid', 'customerid']], on='orderid', how='inner')

dataset = z.groupby(['orderid'])['full_code'].apply(list).values.tolist()

new_list = []

for i in dataset:
    if len(i) > 2:
        new_list.append(i)

len(new_list)
te = TransactionEncoder()
te_ary = te.fit(new_list).transform(new_list)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.4, use_colnames=True)

frequent_itemsets = apriori(df, min_support=0.2, use_colnames=True)
frequent_itemsets = apriori(df, min_support=0.05, use_colnames=True)
te = TransactionEncoder()
te_ary = te.fit(new_list).transform(new_list)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.005, use_colnames=True)

frequent_itemsets = apriori(df, min_support=0.00005, use_colnames=True)
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t' , encoding='latin-1')

# zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

# zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t' , encoding='latin-1')

products = pd.read_csv('/Users/nancy/Downloads/products.txt', sep='\t', encoding='latin-1')

products['full_code'] = products['PRODUCTGROUPCODE'].astype(str) + '-' + products['PRODUCTID'].astype(str)

orders = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t', encoding='latin-1')

orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')

# campaigns = pd.read_csv('/Users/nancy/Downloads/campaigns.txt', sep='\t' , encoding='latin-1')

customers = pd.read_csv('/Users/nancy/Downloads/customers.txt', sep='\t', encoding='latin-1')

x = pd.merge(orderlines[['orderid', 'productid']], products[['PRODUCTID', 'PRODUCTGROUPNAME', 'full_code']],
             left_on='productid', right_on='PRODUCTID', how='inner')

z = pd.merge(x, orders[['orderid', 'customerid']], on='orderid', how='inner')

dataset = z.groupby(['orderid'])['full_code'].apply(list).values.tolist()

new_list = []

for i in dataset:
    if len(i) > 2:
        new_list.append(i)

te = TransactionEncoder()
te_ary = te.fit(new_list).transform(new_list)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.001, use_colnames=True)

te = TransactionEncoder()
te_ary = te.fit(new_list).transform(new_list)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.001, use_colnames=True)

x = pd.merge(orderlines[['orderid', 'productid']], products[['PRODUCTID', 'PRODUCTGROUPNAME', 'full_code']],
             left_on='productid', right_on='PRODUCTID', how='inner')

z = pd.merge(x, orders[['orderid', 'customerid']], on='orderid', how='inner')

dataset = z.groupby(['orderid'])['full_code'].apply(list).values.tolist()

new_list = []

for i in dataset:
    if len(i) > 2:
        new_list.append(i)

te = TransactionEncoder()
te_ary = te.fit(new_list).transform(new_list)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.004, use_colnames=True)

frequent_itemsets = apriori(df, min_support=0.003, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="confidence")
rules.head()
rules.sort_values(by='lift')
r = rules.sort_values(by='lift')
r.head()
rules.columns()
rules.columns
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t' , encoding='latin-1')

# zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

# zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t' , encoding='latin-1')

products = pd.read_csv('/Users/nancy/Downloads/products.txt', sep='\t', encoding='latin-1')

products['full_code'] = products['PRODUCTGROUPCODE'].astype(str) + '-' + products['PRODUCTID'].astype(str)

orders = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t', encoding='latin-1')

orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')

# campaigns = pd.read_csv('/Users/nancy/Downloads/campaigns.txt', sep='\t' , encoding='latin-1')

customers = pd.read_csv('/Users/nancy/Downloads/customers.txt', sep='\t', encoding='latin-1')

x = pd.merge(orderlines[['orderid', 'productid']], products[['PRODUCTID', 'PRODUCTGROUPNAME', 'full_code']],
             left_on='productid', right_on='PRODUCTID', how='inner')

z = pd.merge(x, orders[['orderid', 'customerid']], on='orderid', how='inner')

dataset = z.groupby(['orderid'])['full_code'].apply(list).values.tolist()

new_list = []

for i in dataset:
    if len(i) > 2:
        new_list.append(i)

te = TransactionEncoder()
te_ary = te.fit(new_list).transform(new_list)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.003, use_colnames=True)

rules = association_rules(frequent_itemsets, metric="confidence")

rules.to_csv('rules.csv', index=False)
rules = pd.read_csv('https://github.com/nchelaru/plotly-dashboard/raw/master/rules.csv')

rules = rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']]

x = pd.merge(orderlines[['orderid', 'productid']], products[['PRODUCTID', 'PRODUCTGROUPNAME', 'full_code']],
             left_on='productid', right_on='PRODUCTID', how='inner')

z = pd.merge(x, orders[['orderid', 'customerid']], on='orderid', how='inner')

dataset = z.groupby(['orderid'])['full_code'].apply(list).values.tolist()

new_list = []

for i in dataset:
    if len(i) > 2:
        new_list.append(i)

te = TransactionEncoder()
te_ary = te.fit(new_list).transform(new_list)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.003, use_colnames=True)

import pandas as pd
import plotly.express as px
import numpy as np
import plotly
from plotly import graph_objs as go
import datetime
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

## Import data
zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t', encoding='latin-1')

zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t', encoding='latin-1')

products = pd.read_csv('/Users/nancy/Downloads/products.txt', sep='\t', encoding='latin-1')

products['full_code'] = products['PRODUCTGROUPCODE'].astype(str) + '-' + products['PRODUCTID'].astype(str)

orders = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t', encoding='latin-1')

orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')

campaigns = pd.read_csv('/Users/nancy/Downloads/campaigns.txt', sep='\t', encoding='latin-1')

customers = pd.read_csv('/Users/nancy/Downloads/customers.txt', sep='\t', encoding='latin-1')

x = pd.merge(orderlines[['orderid', 'productid']], products[['PRODUCTID', 'PRODUCTGROUPNAME', 'full_code']],
             left_on='productid', right_on='PRODUCTID', how='inner')

z = pd.merge(x, orders[['orderid', 'customerid']], on='orderid', how='inner')

dataset = z.groupby(['orderid'])['full_code'].apply(list).values.tolist()

new_list = []

for i in dataset:
    if len(i) > 2:
        new_list.append(i)

te = TransactionEncoder()
te_ary = te.fit(new_list).transform(new_list)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.003, use_colnames=True)

rules = association_rules(frequent_itemsets, metric="confidence")

rules = rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']]
x = pd.merge(orderlines[['orderid', 'productid']], products[['PRODUCTID', 'PRODUCTGROUPNAME', 'full_code']],
             left_on='productid', right_on='PRODUCTID', how='inner')

z = pd.merge(x, orders[['orderid', 'customerid']], on='orderid', how='inner')

dataset = z.groupby(['customerid'])['full_code'].apply(list).values.tolist()

new_list = []

for i in dataset:
    if len(i) > 2:
        new_list.append(i)

te = TransactionEncoder()
te_ary = te.fit(new_list).transform(new_list)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.003, use_colnames=True)

rules = association_rules(frequent_itemsets, metric="confidence")

rules.write_csv('rules.csv', index=False)
rules[['antecedents', 'consequents']] == rules[['antecedents', 'consequents']].astype(str)
rules = rules.replace('frozenset({', '')
rules['antecedents'] = rules['antecedents'].replace('frozenset({', '')
rules.info()
rules['antecedents'].dtype()
rules['antecedents'].dtype
rules['antecedents'] == rules['antecedents'].astype(str)

rules['antecedents'] = rules['antecedents'].replace('frozenset({', '')

rules['antecedents'].split('frozenset({')
rules['antecedents'].str.split('frozenset({')
rules['antecedents'].str.split('frozenset')
rules['antecedents'].str.split('frozenset(')
rules['antecents'] = rules['antecedents'].str.split('frozenset')
rules = pd.read_csv('https://github.com/nchelaru/plotly-dashboard/raw/master/rules.csv')
rules["antecedents"] = rules["antecedents"].apply(lambda x: ', '.join(list(x))).astype("unicode")
rules["antecedents"] = rules["antecedents"].apply(lambda x: list(x)).astype("unicode")
x = pd.merge(orderlines[['orderid', 'productid']], products[['PRODUCTID', 'PRODUCTGROUPNAME', 'full_code']],
             left_on='productid', right_on='PRODUCTID', how='inner')

z = pd.merge(x, orders[['orderid', 'customerid']], on='orderid', how='inner')

dataset = z.groupby(['customerid'])['full_code'].apply(list).values.tolist()

new_list = []

for i in dataset:
    if len(i) > 2:
        new_list.append(i)

te = TransactionEncoder()
te_ary = te.fit(new_list).transform(new_list)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.003, use_colnames=True)

rules = association_rules(frequent_itemsets, metric="confidence")

rules["antecedents"] = rules["antecedents"].apply(lambda x: list(x)[0]).astype("unicode")
rules["consequents"] = rules["consequents"].apply(lambda x: list(x)).astype("unicode")
x = pd.merge(orderlines[['orderid', 'productid']], products[['PRODUCTID', 'PRODUCTGROUPNAME', 'full_code']],
             left_on='productid', right_on='PRODUCTID', how='inner')

z = pd.merge(x, orders[['orderid', 'customerid']], on='orderid', how='inner')

dataset = z.groupby(['customerid'])['full_code'].apply(list).values.tolist()

new_list = []

for i in dataset:
    if len(i) > 2:
        new_list.append(i)

te = TransactionEncoder()
te_ary = te.fit(new_list).transform(new_list)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.003, use_colnames=True)

rules = association_rules(frequent_itemsets, metric="confidence")

rules["antecedents"] = rules["antecedents"].apply(lambda x: list(x)).astype("unicode")

rules["consequents"] = rules["consequents"].apply(lambda x: list(x)).astype("unicode")

rules.to_csv('rules.csv', index=False)
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t' , encoding='latin-1')

# zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

# zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t' , encoding='latin-1')

products = pd.read_csv('/Users/nancy/Downloads/products.txt', sep='\t', encoding='latin-1')

products['full_code'] = products['PRODUCTGROUPCODE'].astype(str) + '-' + products['PRODUCTID'].astype(str)

orders = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t', encoding='latin-1')

orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')

# campaigns = pd.read_csv('/Users/nancy/Downloads/campaigns.txt', sep='\t' , encoding='latin-1')

customers = pd.read_csv('/Users/nancy/Downloads/customers.txt', sep='\t', encoding='latin-1')

orders['orderdate'].max()
orders.indo()
orders.info()
orders['orderdate'] = pd.to_datetime(orders['orderdate'])

last_day = orders['orderdate'].max()

rfm = orders.groupby('customerid').agg({'orderdate': lambda date: (last_day - date.max()).days,
                                        'orderid': lambda num: len(num),
                                        'totalprice': lambda price: price.sum()})

rfm = orders.groupby('customerid').agg({'orderdate': lambda date: (last_day - date.max()).days,
                                        'orderid': 'count',
                                        'totalprice': lambda price: price.sum()})

rfm.columns()
rfm.columns
rfm['orderid'].nunique()
orders.groupby('customerid')['orderid'].count()
customers['customerid'].nunique()
orders['customerid'].nunique()
grouped = orders.groupby(['zipcode'])['city', 'state', 'totalprice'].agg('sum').reset_index()

merged = pd.merge(grouped, zipcounty[['zipcode', 'latitude', 'longitude']], on='zipcode')

merged.columns = ['zipcode', 'totalprice', 'Latitude', 'Longitude']

merged = merged[merged['totalprice'] > 0]

merged['log_totalprice'] = np.log(merged['totalprice'])

grouped = orders.groupby(['zipcode'])['city', 'state', 'totalprice'].agg('sum').reset_index()

grouped = orders.groupby(['city', 'state', 'zipcode'])['totalprice'].agg('sum').reset_index()

grouped = orders.groupby(['city', 'state', 'zipcode'])['totalprice'].agg('sum')
merged = pd.merge(grouped, zipcounty[['zipcode', 'latitude', 'longitude']], on='zipcode').reset_index()
grouped = orders.groupby(['city', 'state', 'zipcode'])['totalprice'].agg('sum').reset_index(inplace=True)
grouped = orders.groupby(['city', 'state', 'zipcode'])['totalprice'].agg('sum').reset_index()
merged = merged[merged['totalprice'] > 0]

merged['log_totalprice'] = np.log(merged['totalprice'])

merged['location'] = merged['city'].astype(str) + ", " + merged['state'].astype('str')

merged['location'] = merged['city'].astype(str) + ", " + merged['state'].astype('str')
grouped = orders.groupby(['zipcode'])['totalprice'].agg('sum').reset_index()

merged = pd.merge(grouped, zipcounty[['zipcode', 'latitude', 'longitude']], on='zipcode')

merged_2 = pd.merge(merged, orders[['zipcode', 'city', 'state']], on='zipcode', how='inner')

merged_2['zipcode'].value_counts()
grouped = orders.groupby(['zipcode'])['totalprice'].agg('sum').reset_index()
merged = pd.merge(grouped, zipcounty[['zipcode', 'latitude', 'longitude']], on='zipcode')
merged_2 = pd.merge(merged, orders[['zipcode', 'city', 'state']], on='zipcode', how='left')
merged_2 = merged_2.drop_duplicates(subset=['zipcode', 'latitude', 'longitude'], keep='First', inplace=True)
merged_2 = merged_2.drop_duplicates(subset=['zipcode', 'latitude', 'longitude'], keep='first', inplace=True)
grouped = orders.groupby(['zipcode'])['totalprice'].agg('sum').reset_index()

merged = pd.merge(grouped, zipcounty[['zipcode', 'latitude', 'longitude']], on='zipcode')

merged_2 = pd.merge(merged, orders[['zipcode', 'city', 'state']], on='zipcode', how='left')

merged_2.shape()
merged_2.shape
merged_2['zipcode'].nunique()
merged_3 = merged_2.drop_duplicates(subset=['zipcode', 'latitude', 'longitude'], keep='first')
merged_3['location'] = merged_3['zipcode'].astype(str) + '-' + merged_3['city'].astype(str) + ", " + merged_3[
    'state'].astype('str')

merged_3 = merged_3[merged_3['totalprice'] > 0]

merged_3['log_totalprice'] = np.log(merged_3['totalprice'])

import pandas as pd
import plotly.express as px
import numpy as np
import plotly
from plotly import graph_objs as go
import datetime
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

## Import data
zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t', encoding='latin-1')

zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t', encoding='latin-1')

products = pd.read_csv('/Users/nancy/Downloads/products.txt', sep='\t', encoding='latin-1')

products['full_code'] = products['PRODUCTGROUPCODE'].astype(str) + '-' + products['PRODUCTID'].astype(str)

orders = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t', encoding='latin-1')

orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')

campaigns = pd.read_csv('/Users/nancy/Downloads/campaigns.txt', sep='\t', encoding='latin-1')

customers = pd.read_csv('/Users/nancy/Downloads/customers.txt', sep='\t', encoding='latin-1')

orders['orderyear'] = orders['orderdate'].dt.year
orders['orderyear'] = pd.to_datetime(orders['orderdate']).dt.year
grouped = orders.groupby(['zipcode', 'orderyear'])['totalprice'].agg('sum').reset_index()
merged = pd.merge(grouped, zipcounty[['zipcode', 'latitude', 'longitude']], on='zipcode')

merged_2 = pd.merge(merged, orders[['zipcode', 'city', 'state']], on='zipcode', how='left')

merged_3 = merged_2.drop_duplicates(subset=['zipcode', 'latitude', 'longitude'], keep='first')

merged_3['location'] = merged_3['zipcode'].astype(str) + '-' + merged_3['city'].astype(str) + ", " + merged_3[
    'state'].astype('str')

merged_3 = merged_3[merged_3['totalprice'] > 0]

merged_3['log_totalprice'] = np.log(merged_3['totalprice'])

merged_3.columns = ['Zipcode', 'TotalSpent', 'Latitude', 'Longitude', 'City', 'State', 'Location', 'Log10(TotalSpent)']

merged_3.columns = ['Zipcode', 'Year', 'TotalSpent', 'Latitude', 'Longitude', 'City', 'State', 'Location',
                    'Log10(TotalSpent)']

orders['orderyear'] = pd.to_datetime(orders['orderdate']).dt.year

grouped = orders.groupby(['zipcode', 'orderyear'])['totalprice'].agg('sum').reset_index()

merged = pd.merge(grouped, zipcounty[['zipcode', 'latitude', 'longitude']], on='zipcode')

merged_2 = pd.merge(merged, orders[['zipcode', 'city', 'state']], on='zipcode', how='left')

merged_3 = merged_2.drop_duplicates(subset=['zipcode', 'latitude', 'longitude'], keep='first')

merged_3['location'] = merged_3['zipcode'].astype(str) + '-' + merged_3['city'].astype(str) + ", " + merged_3[
    'state'].astype('str')

merged_3 = merged_3[merged_3['totalprice'] > 0]

merged_3['log_totalprice'] = np.log(merged_3['totalprice'])

merged_3.columns = ['Zipcode', 'Year', 'TotalSpent', 'Latitude', 'Longitude', 'City', 'State', 'Location',
                    'Log10(TotalSpent)']

px.set_mapbox_access_token("pk.eyJ1IjoibmQ4MjMiLCJhIjoiY2p1aDNheXltMHNuNTN6bng2Mjc0a2ZyOSJ9.aJwWqjS3PZcYKVckxisUNg")

fig = px.scatter_mapbox(merged_3, lat="Latitude", lon="Longitude", size="Log10(TotalSpent)",
                        color="Log10(TotalSpent)", color_continuous_scale=px.colors.diverging.RdYlGn[::-1],
                        zoom=2, size_max=10, hover_name='Location', hover_data='TotalSpent',
                        animation_frame='Year', animation_group='Year', )

fig = px.scatter_mapbox(merged_3, lat="Latitude", lon="Longitude", size="Log10(TotalSpent)",
                        color="Log10(TotalSpent)", color_continuous_scale=px.colors.diverging.RdYlGn[::-1],
                        zoom=2, size_max=10, hover_name='Location', hover_data='TotalSpent',
                        animation_frame='Year', animation_group='Year')
merged_3.columns

fig = px.scatter_mapbox(merged_3, lat="Latitude", lon="Longitude", size="Log10(TotalSpent)",
                        color="Log10(TotalSpent)", color_continuous_scale=px.colors.diverging.RdYlGn[::-1],
                        zoom=2, size_max=10, hover_name='Location',
                        animation_frame='Year', animation_group='Year')
merged_3['Year'] = merged_3['Year'].astype(int)
merged_3.sort_values(by='Year', inplace=True)
orderlines['billyear'] = pd.to_datetime(orderlines['billdate']).dt.year

orderlines['billyear'] = orderlines['billyear'].astype(int)

merged = pd.merge(orderlines[['productid', 'totalprice']], products[['PRODUCTID', 'PRODUCTGROUPNAME']],
                  left_on='productid', right_on='PRODUCTID', how='inner')

orderlines['billyear'] = pd.to_datetime(orderlines['billdate']).dt.year

orderlines['billyear'] = orderlines['billyear'].astype(int)

merged = pd.merge(orderlines[['productid', 'billyear', 'totalprice']], products[['PRODUCTID', 'PRODUCTGROUPNAME']],
                  left_on='productid', right_on='PRODUCTID', how='inner')

merged_2 = pd.merge(merged_1, zipcounty[['zipcode', 'latitude', 'longitude']], on='zipcode')

z = merged_2.groupby(['zipcode', 'year', 'channel'])['totalprice'].mean()

merged_2 = pd.merge(merged_1, zipcounty[['zipcode', 'latitude', 'longitude']], on='zipcode')

z = merged_2.groupby(['zipcode', 'orderyear', 'channel'])['totalprice'].mean()

z = z.unstack(level=-1)

z.fillna(0, inplace=True)

z['Max_chnl_val'] = (z.max(axis=1) / z.sum(axis=1)) * 100

z['Max_chnl'] = z.drop('Max_chnl_val', axis=1, inplace=False).idxmax(axis=1)

z['zipcode'] = z.index

z.reset_index(drop=True, inplace=True)

z = z[~z['Max_chnl_val'].isnull()]

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t' , encoding='latin-1')

# zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t', encoding='latin-1')

zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t', encoding='latin-1')
import pyproj

geodesic = pyproj.Geod(ellps='WGS84')
fwd_azimuth, back_azimuth, distance = geodesic.inv(37.0902, 95.7129, 18.36603, -65.70814)

pip
install
geographiclib
from geographiclib.geodesic import Geodesic


def get_bearing(lat1, lat2, long1, long2):
    brng = Geodesic.WGS84.Inverse(lat1, long1, lat2, long2)['azi1']
    return brng


get_bearing(37.0902, 95.7129, 18.36603, -65.70814)

get_bearing(37.0902, 18.36603, 95.7129, -65.70814)

get_bearing(37.0902, 95.7129, 18.36603, -65.70814)
get_bearing(95.7129, 37.0902, 18.36603, -65.70814)
get_bearing(95.7129, 18.36603, 37.0902, -65.70814)
import pyproj


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


calculate_initial_compass_bearing([95.7129, 37.0902], [53.6880, 32.4279])

ptA = (95.7129, 37.0902)

ptB = (53.6880, 32.4279)

calculate_initial_compass_bearing(ptA, ptB)

import math

ptA = (95.7129, 37.0902)

ptB = (53.6880, 32.4279)

calculate_initial_compass_bearing(ptA, ptB)

import pandas as pd
import plotly.express as px
import numpy as np
import plotly
from plotly import graph_objs as go
import datetime
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

## Import data
zipcounty = pd.read_csv('/Users/nancy/Downloads/zipcounty.txt', sep='\t', encoding='latin-1')

zipcounty['zipcode'] = zipcounty['zipcode'].astype(str)

zipcensus = pd.read_csv('/Users/nancy/Downloads/ZipCensus_ss.txt', sep='\t', encoding='latin-1')

products = pd.read_csv('/Users/nancy/Downloads/products.txt', sep='\t', encoding='latin-1')

products['full_code'] = products['PRODUCTGROUPCODE'].astype(str) + '-' + products['PRODUCTID'].astype(str)

orders = pd.read_csv('/Users/nancy/Downloads/orders.txt', sep='\t', encoding='latin-1')

orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')

campaigns = pd.read_csv('/Users/nancy/Downloads/campaigns.txt', sep='\t', encoding='latin-1')

customers = pd.read_csv('/Users/nancy/Downloads/customers.txt', sep='\t', encoding='latin-1')

ptA = (95.7129, 37.0902)

ptB = (-80.18722, 25.81428)

calculate_initial_compass_bearing(ptA, ptB)


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
    # initial_bearing = math.degrees(initial_bearing)
    # compass_bearing = (initial_bearing + 360) % 360

    # return compass_bearing

    return initial_bearing


ptA = (95.7129, 37.0902)

ptB = (-80.18722, 25.81428)

calculate_initial_compass_bearing(ptA, ptB)


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
    # compass_bearing = (initial_bearing + 360) % 360

    # return compass_bearing

    return initial_bearing


ptA = (95.7129, 37.0902)

ptB = (-80.18722, 25.81428)

calculate_initial_compass_bearing(ptA, ptB)

import pyproj

geodesic = pyproj.Geod(ellps='WGS84')
fwd_azimuth, back_azimuth, distance = geodesic.inv(95.7129, 37.0902, -80.18722, 25.81428)


def angleFromCoordinate(lat1, long1, lat2, long2):
    dLon = (long2 - long1)

    y = math.sin(dLon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dLon)

    brng = math.atan2(y, x)

    brng = math.degrees(brng)
    brng = (brng + 360) % 360
    brng = 360 - brng  # count degrees clockwise - remove to make counter-clockwise

    return brng


angleFromCoordinate(95.7129, 37.0902, -80.18722, 25.81428)

angleFromCoordinate(37.0902, 95.7129, -80.18722, 25.81428)
angleFromCoordinate(37.0902, 95.7129, 25.81428, -80.18722)
angleFromCoordinate(37.0902, -95.7129, 25.81428, -80.18722)


def angleFromCoordinate(lat1, long1, lat2, long2):
    dLon = (long2 - long1)

    y = math.sin(dLon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dLon)

    brng = math.atan2(y, x)

    brng = math.degrees(brng)
    brng = (brng + 360) % 360
    brng = 360 - brng  # count degrees clockwise - remove to make counter-clockwise

    return brng


angleFromCoordinate(37.0902, -95.7129, 25.81428, -80.18722)


def angleFromCoordinate(lat1, long1, lat2, long2):
    dLon = (long2 - long1)

    y = math.sin(dLon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dLon)

    brng = math.atan2(y, x)

    brng = math.degrees(brng)
    brng = (brng + 360) % 360
    # brng = 360 - brng # count degrees clockwise - remove to make counter-clockwise

    return brng


angleFromCoordinate(37.0902, -95.7129, 25.81428, -80.18722)






final.stack(level=1)
final.stack(level=0)
final.set_index('polar')
final.set_index('polar', inplace=True)
final.stack(level=-1)
final.unstack(level=-1)
final.head()
final.reset_index()
final.groupby('polar')['totalprice'].mean()
final.groupby('polar').mean()
mean_final = final.groupby('polar').mean()
mean_final.reset_index()
mean_final = mean_final.reset_index()
df.melt(id_vars=['polar'],
        var_name="Channel",
        value_name="Value")
mean_final.melt(id_vars=['polar'],
                var_name="Channel",
                value_name="Value")
a = mean_final.melt(id_vars=['polar'],
                    var_name="Channel",
                    value_name="Value")
a.head()
fig = px.bar_polar(a, r="Channel", theta="polar",
                   color="Value", template="plotly_dark",
                   color_discrete_sequence=px.colors.sequential.Plasma[-2::-1])
fig.show()
a.to_csv('a.csv', index=False)
a = pd.read_csv('a.csv')
fig = px.bar_polar(a, r="Channel", theta="polar",
                   color="Value", template="plotly_dark",
                   color_discrete_sequence=px.colors.sequential.Plasma[-2::-1])
