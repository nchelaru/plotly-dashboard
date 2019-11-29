import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from graphs import *
from dash.dependencies import Input, Output, State
import datetime

## Import data
orders_df = orders_data()

df = assn_rules()

# merged_3 = pd.read_csv('./map_data_lite.csv')
#
# merged_3['Date'] = pd.to_datetime(merged_3['Date'])
#
# merged_3['Date'] = merged_3['Date'].dt.date
#
# merged_3 = merged_3[['Date', 'Year', 'TotalSpent', 'Latitude', 'Longitude', 'Zipcode', 'Location', 'City', 'State']]
#
# merged_3.columns = ['OrderDate', 'Year', 'TotalAmount', 'Latitude', 'Longitude', 'ZipCode', 'Location', 'City', 'State']
#
# merged_3['Log(TotalRevenue)'] = np.log(merged_3['TotalAmount'])
#
# merged_3 = merged_3.replace([np.inf, -np.inf], np.nan)
#
# merged_3 = merged_3.fillna(0)
#
# merged_3 = merged_3.sort_values(by='TotalAmount', ascending=False)
#
# merged_3.to_csv('./map_data_app.csv', index=False)

merged_3 = pd.read_csv('./map_data_app.csv')

## App

navbar = dbc.Container(
    dbc.Navbar(
        [
            dbc.NavbarBrand(dbc.Row([
                dbc.Col(html.Img(src="./assets/logo.png", height="50px"), width=3),
                dbc.Col(html.H3("SaleVenture Inc.", style={'margin-top':'10px'}))
            ])
            ),
            dbc.Nav(
                [
                    dbc.Button("About", color="success", id='open'),
                    dbc.Modal(
                                [
                                    dbc.ModalHeader("Welcome!"),
                                    dbc.ModalBody(dcc.Markdown('''

                                    This is a sample sales dashboard for a fictional company, SalesVenture Inc., made using the Plotly Dash framework.
                                     
                                    The data is taken from the datasets accompanying the book *Data Analysis Using SQL and Excel*
                                    by Gordon S. Linoff, which can be downloaded [here](https://www.wiley.com/en-ca/Data+Analysis+Using+SQL+and+Excel%2C+2nd+Edition-p-9781119021438#downloads-section).
                                    Due to hosting limits, a *subset* of the available data are used in certain sections. In addition, simulated data are used where needed.

                                    Please go to the [Github repo](https://github.com/nchelaru/plotly-dashboard) for the source code. Also, to see my other work in Python and R, 
                                    please visit my portfolio at http://nancychelaru.rbind.io/.

                                    Hope you enjoy your stay!

                                    ''')),
                                    dbc.ModalFooter(
                                        dbc.Button("Close", id="close", className="ml-auto")
                                    ),
                                ],
                                id="modal",
                                size='xl'
                            ),
                ],
                navbar=True,
                className="ml-auto",
            ),
        ], sticky="top",
    ), fluid=True)


card_content = [
    dbc.CardHeader("Card header"),
    dbc.CardBody(
        [
            html.H5("Card title", className="card-title"),
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",
            ),
        ]
    ),
]

tab1_content = dbc.Container(
    [html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card([
                            dbc.CardBody(
                                [
                                    html.H2(datetime.datetime(2016, 9, 19).strftime('%A'),
                                            style={'color':'#72bcd4', 'text-align':'center', 'vertical-align':'middle', 'fontWeight': 'bold'}),
                                    html.H3(datetime.datetime(2016, 9, 19).strftime('%B %d, %Y'),
                                            style={'color':'black', 'text-align':'center', 'vertical-align':'middle', 'fontWeight': 'bold'})
                                ]
                            ),
                        ], color="light", outline=True, style={'height':'12vh', 'border': '0'}), width=3),
                    dbc.Col(dbc.Card([
                        dbc.CardBody(
                            [
                                dcc.Graph(figure=gauge_revenue(), style={'height': '10vh'})
                            ]
                        ),
                    ], color="primary", outline=True, style={'height': '13vh'}), width=3),
                    dbc.Col(dbc.Card([
                        dbc.CardBody(
                            [
                                dcc.Graph(figure=gauge_orders(), style={'height': '10vh'})
                            ]
                        ),
                    ], color="warning", outline=True, style={'height': '13vh'}), width=3),
                    dbc.Col(dbc.Card([
                        dbc.CardBody(
                            [
                                dcc.Graph(figure=gauge_units(), style={'height': '10vh'})
                            ]
                        ),
                    ], color="danger", outline=True, style={'height': '13vh'}), width=3)
                ], className='mb-4', style={'height': '14vh'}
            ),
            dbc.Row(
                [
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader("Revenue by product categories - September 2016",
                                           style={'color':'white', 'fontWeight': 'bold', 'backgroundColor': "#D96383"}),
                            dbc.CardBody(
                                [
                                    dcc.Graph(figure=bullet_chart(), style={'height': 'inherit', 'width': 'inherit'})
                                ]
                            ),
                            dbc.CardFooter([
                                    html.P("The green bar indicates total revenue in each product category in 2016 September. The diamond marker and the orange bar show the corresponding values in 2016 Augst and 2015 September, respectively.",
                                           style={'font-style':'italic', 'font-size':'13px'})
                            ])
                        ],  color="light", outline=True),
                        html.Br(),
                        dbc.Card([
                            dbc.CardHeader("Overview - August 2016",
                                           style={'color':'white', 'fontWeight': 'bold',  'backgroundColor': "#4AB471"}),
                            dbc.CardBody(
                                [
                                    dcc.Graph(figure=waterfall_chart(), style={'height': 'inherit', 'width': 'inherit'})
                                ]
                            ),
                        ],  color="light", outline=True)
                    ], width=6),
                    dbc.Col(
                        dbc.Card([
                            dbc.CardHeader("Customer orders - September 2016",
                                           style={'color':'white', 'fontWeight': 'bold', 'backgroundColor': "#f1a336"}),
                            dbc.CardBody(
                                [
                                    dash_table.DataTable(
                                        id='table-sorting-filtering',
                                        columns=[
                                            {'name': i, 'id': i, 'deletable': False} for i in orders_df.columns
                                        ],
                                        style_table={'overflowX': 'scroll',
                                                     'overflowY': 'scroll'},
                                        style_cell={
                                            'font-family':'sans-serif',
                                            'color':'black'
                                        },
                                        style_header={
                                            'backgroundColor': "#F3AE4E",
                                            'color':'white'
                                        },
                                        page_current=0,
                                        page_size=32,
                                        page_action='custom',
                                        filter_action='custom',
                                        filter_query='',
                                        sort_action='custom',
                                        sort_mode='multi',
                                        sort_by=[],
                                        style_as_list_view=True
                                    )
                                ]
                            ),
                        ], color="light", outline=True, className='h-100'),
                        width=6)
                ],
                className="mb-4", style={'height': '25vh'}
            )
        ]
    )
    ],
    className="mt-4", fluid=True
)

tab2_content = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card([
                    dbc.CardHeader("Daily total revenue by sales territories (from 2010 to 2016)",
                                   style={'backgroundColor':'#717ECD', 'color':'white', 'fontWeight': 'bold'}),
                    dbc.CardBody(
                        [   dcc.Markdown('''*Filtering data in this table renders the resulting dataset in the map and timeseries plot. 
                                            See [here](https://dash.plot.ly/datatable/filtering) for filtering syntax.* '''),
                            dash_table.DataTable(
                                    id='datatable-interactivity',
                                    columns=[
                                        {"name": i, "id": i, "deletable": False, "selectable": False} for i in ['OrderDate', 'TotalAmount', 'City', 'State', 'ZipCode']
                                    ],
                                    data=merged_3.to_dict('records'),
                                    editable=False,
                                    filter_action="native",
                                    sort_action="native",
                                    sort_mode="multi",
                                    column_selectable=False,
                                    row_deletable=False,
                                    selected_columns=[],
                                    selected_rows=[],
                                    page_action="native",
                                    page_current= 0,
                                    page_size= 13,
                                    style_header={
                                            'backgroundColor': "#8684d4",
                                            'color':'white',
                                            'fontWeight': 'bold'},
                                    style_table={'overflowX': 'scroll',
                                                 'overflowY': 'scroll'},
                                    style_cell={
                                            'font-family':'sans-serif',
                                            'color':'black',
                                            'font-size': 13
                                        },
                                )
                        ]
                    ),
                ], className='h-100', color="light", outline=True), width=5),
                dbc.Col(dbc.Card([
                    dbc.CardHeader("Geographic distribution of sales territories",
                                   style={'backgroundColor':'#F3AE4E', 'color':'white', 'fontWeight':'bold'}),
                    dbc.CardBody(
                        id='datatable-interactivity-container'
                    ),
                ], className='h-100', color="light", outline=True), width=7),
            ],
            className="mb-4",
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Card([
                    dbc.CardHeader("Seasonal pattern in sales revenue",
                                   style={'backgroundColor':'#CF5C60', 'color':'white', 'fontWeight':'bold'}),
                    dbc.CardBody(
                        id='datatable-interactivity-container2'
                    ),
                ], className="h-100", color="light", outline=True), width=12)
            ],
            className="mt-4"
        )
    ], fluid=True,  style={'height':'80vh'}
)

dates = [2010, 2011, 2012, 2013, 2014, 2015, 2016]

tab3_content = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Relationship between product unit price and order size", style={'color':'white', 'fontWeight': 'bold', 'backgroundColor':'#717ECD'}),
                dbc.CardBody(dcc.RangeSlider(id = 'slider',
                                        marks = ['2010', '2011', '2012', '2013', '2014', '2015', '2016'],
                                        min = 0,
                                        max = 6,
                                        value = [0])),
                dbc.CardBody(id='scatter')
            ], color="light", className='h-100', outline=True),
        ], width=5),
    html.Br(),
    dbc.Col([
        dbc.Card([
            dbc.CardHeader("Market basket analysis by association rule mining", style={'color':'white', 'fontWeight': 'bold', 'backgroundColor':'#D96383'}),
            dbc.CardBody(
                [
                    dash_table.DataTable(
                        id='table-sorting-filtering2',
                        columns=[
                            {'name': i, 'id': i, 'deletable': False} for i in df.columns
                        ],
                        style_table={'overflowX': 'scroll',
                                     'overflowY': 'scroll'},
                        style_cell={
                            'minWidth': '80px',
                            'font-family':'sans-serif',
                            'color':'black'
                        },
                        style_header={
                                'backgroundColor': "#de7893",
                                'color':'white',
                                'fontWeight': 'bold'
                            },
                        page_current=0,
                        page_size=10,
                        page_action='custom',
                        filter_action='custom',
                        filter_query='',
                        sort_action='custom',
                        sort_mode='multi',
                        sort_by=[]
                    )
                ]
            ),
        ], color="light", outline=True)
        ,
        html.Br(),
        dbc.Card([
            dbc.CardHeader("Daily revenue by product group",
                           style={'color':'white', 'fontWeight': 'bold', 'backgroundColor':'#4AB471'}),
            dbc.CardBody(
                [
                    dcc.Graph(figure=cat_month_heatmap(), style={'width': '55vw', 'height': '45vh'})
                ]
            ),
        ], color="light", outline=True)
        ], width=7)])
], fluid = True)

tab4_content = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Revenue breakdown by campaign channel and product group",
                               style={'color':'white', 'fontWeight': 'bold', 'backgroundColor':'#2A94D6'}),
                dbc.CardBody(dcc.RangeSlider(id = 'slider2',
                                        marks = ['2010', '2011', '2012', '2013', '2014', '2015', '2016'],
                                        min = 0,
                                        max = 6,
                                        value = [0])),
                dbc.CardBody(id='para_coord'),
            ], color="light", outline=True, className='h-100')
        ], width=7),
        dbc.Col(
            dbc.Card([
                dbc.CardHeader("Total revenue derived from each campaign channel by US region",
                               style={'color':'white', 'fontWeight': 'bold', 'backgroundColor':'#4AB471'}),
                dbc.CardBody(
                    [
                        dcc.Graph(figure=polar_plot(), style={'height': 'inherit', 'width':'38vw'})
                    ]
                ),
            ], color="light", outline=True, className='h-100'), width=5)
    ]),
    html.Br(),
    dbc.Row(
        dbc.Col(
            dbc.Card([
                dbc.CardHeader("Seasonal change in revenue derived from each campaign channel",
                               style={'backgroundColor':'#F0F1F2', 'color':'black', 'fontWeight': 'bold'}),
                dbc.CardBody(
                    [
                        dcc.Graph(figure=stacked_area(), style={'width': '95vw'})
                    ]
                ),
            ], color="light", outline=True)
        )
    )
], fluid=True)

FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MINTY,  FONT_AWESOME])

app.title = 'Dashboard'

server = app.server

tabs = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="KPIs",
                labelClassName="text-success", tab_style={'width': '25vw'},
                label_style={"font-size": "22px", "font-weight": "bold", "text-align": 'center'}
                ),
        dbc.Tab(tab2_content, label="Sales territories",
                labelClassName="text-danger", tab_style={'width': '24vw'},
                label_style={"font-size": "22px", "font-weight": "bold", "text-align": 'center'}
                ),
        dbc.Tab(tab3_content, label="Products",
                labelClassName="text-warning", tab_style={'width': '24vw'},
                label_style={"font-size": "22px", "font-weight": "bold", "text-align": 'center'}
                ),
        dbc.Tab(tab4_content, label="Marketing campaigns",
                labelClassName="text-info", tab_style={'width': '24vw'},
                label_style={"font-size": "22px", "font-weight": "bold", "text-align": 'center'}
                )
    ], style={'margin':'20px'}
)

# app.layout = html.Div([navbar, tabs])

app.layout = html.Div([navbar, tabs], style={'height':'100vh'})

@ app.callback(
Output('table-sorting-filtering', 'data'),
[Input('table-sorting-filtering', "page_current"),
Input('table-sorting-filtering', "page_size"),
Input('table-sorting-filtering', 'sort_by'),
Input('table-sorting-filtering', 'filter_query')])
def update_table(page_current, page_size, sort_by, filter):
    filtering_expressions = filter.split(' && ')
    dff = orders_df
    for filter_part in filtering_expressions:
        col_name, operator, filter_value = split_filter_part(filter_part)

        if operator in ('eq', 'ne', 'lt', 'le', 'gt', 'ge'):
            # these operators match pandas series operator method names
            dff = dff.loc[getattr(dff[col_name], operator)(filter_value)]
        elif operator == 'contains':
            dff = dff.loc[dff[col_name].str.contains(filter_value)]
        elif operator == 'datestartswith':
            # this is a simplification of the front-end filtering logic,
            # only works with complete fields in standard format
            dff = dff.loc[dff[col_name].str.startswith(filter_value)]

    if len(sort_by):
        dff = dff.sort_values(
            [col['column_id'] for col in sort_by],
            ascending=[
                col['direction'] == 'asc'
                for col in sort_by
            ],
            inplace=False
        )

    page = page_current
    size = page_size
    return dff.iloc[page * size: (page + 1) * size].to_dict('records')


@app.callback(
Output('table-sorting-filtering2', 'data'),
[Input('table-sorting-filtering2', "page_current"),
Input('table-sorting-filtering2', "page_size"),
Input('table-sorting-filtering2', 'sort_by'),
Input('table-sorting-filtering2', 'filter_query')])
def update_table_assn(page_current, page_size, sort_by, filter):
    filtering_expressions = filter.split(' && ')
    dff = df
    for filter_part in filtering_expressions:
        col_name, operator, filter_value = split_filter_part(filter_part)

        if operator in ('eq', 'ne', 'lt', 'le', 'gt', 'ge'):
            # these operators match pandas series operator method names
            dff = dff.loc[getattr(dff[col_name], operator)(filter_value)]
        elif operator == 'contains':
            dff = dff.loc[dff[col_name].str.contains(filter_value)]
        elif operator == 'datestartswith':
            # this is a simplification of the front-end filtering logic,
            # only works with complete fields in standard format
            dff = dff.loc[dff[col_name].str.startswith(filter_value)]

    if len(sort_by):
        dff = dff.sort_values(
            [col['column_id'] for col in sort_by],
            ascending=[
                col['direction'] == 'asc'
                for col in sort_by
            ],
            inplace=False
        )

    page = page_current
    size = page_size
    return dff.iloc[page * size: (page + 1) * size].to_dict('records')




@app.callback(
    Output('datatable-interactivity-container', "children"),
    [Input('datatable-interactivity', "derived_virtual_data"),
     Input('datatable-interactivity', "derived_virtual_selected_rows")])
def update_graphs(rows, derived_virtual_selected_rows):
    # When the table is first rendered, `derived_virtual_data` and
    # `derived_virtual_selected_rows` will be `None`. This is due to an
    # idiosyncracy in Dash (unsupplied properties are always None and Dash
    # calls the dependent callbacks when the component is first rendered).
    # So, if `rows` is `None`, then the component was just rendered
    # and its value will be the same as the component's dataframe.
    # Instead of setting `None` in here, you could also set
    # `derived_virtual_data=df.to_rows('dict')` when you initialize
    # the component.
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []

    dff = merged_3 if rows is None else pd.DataFrame(rows)

    grouped = dff.groupby(['ZipCode', 'OrderDate', 'Latitude', 'Longitude', 'Location', 'City', 'State', 'Year'])['TotalAmount'].sum().reset_index()

    grouped = grouped[grouped['TotalAmount'] > 0]

    grouped['Log(TotalRevenue)'] = np.log(grouped['TotalAmount'])



    return [
        dcc.Graph(
            figure=map(grouped),
            style={'width':'55vw', 'height':'inherit'}
        )
    ]


@app.callback(
    Output('datatable-interactivity', 'style_data_conditional'),
    [Input('datatable-interactivity', 'selected_columns')]
)
def update_styles(selected_columns):
    return [{
        'if': { 'column_id': i },
        'background_color': '#D2F3FF'
    } for i in selected_columns]

@app.callback(
    Output('datatable-interactivity-container2', "children"),
    [Input('datatable-interactivity', "derived_virtual_data"),
     Input('datatable-interactivity', "derived_virtual_selected_rows")])
def update_graphs(rows, derived_virtual_selected_rows):
    # When the table is first rendered, `derived_virtual_data` and
    # `derived_virtual_selected_rows` will be `None`. This is due to an
    # idiosyncracy in Dash (unsupplied properties are always None and Dash
    # calls the dependent callbacks when the component is first rendered).
    # So, if `rows` is `None`, then the component was just rendered
    # and its value will be the same as the component's dataframe.
    # Instead of setting `None` in here, you could also set
    # `derived_virtual_data=df.to_rows('dict')` when you initialize
    # the component.
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []

    dff = merged_3 if rows is None else pd.DataFrame(rows)

    grouped = dff.groupby('OrderDate')['TotalAmount'].sum().reset_index()

    return [
        dcc.Graph(
            figure=sales_timeline(grouped),
            style={'width':'95vw'}
        )
    ]

@app.callback(Output('scatter', 'children'),
             [Input('slider', 'value')])
def update_figure(X):
    # orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')
    #
    # orderlines['billyear'] = pd.to_datetime(orderlines['billdate']).dt.year
    #
    # orderlines = orderlines[orderlines['billyear'] > 2009]
    #
    # orderlines['billyear'] = orderlines['billyear'].astype(int)
    #
    # merged = pd.merge(orderlines, products[['PRODUCTID', 'PRODUCTGROUPNAME']],
    #                   left_on='productid', right_on='PRODUCTID', how='inner')
    #
    # merged = merged[~merged['PRODUCTGROUPNAME'].isnull()]
    #
    # merged = merged[merged['PRODUCTGROUPNAME'] != 'FREEBIE']

    merged = pd.read_csv('./scatter_plot.csv')

    merged = merged[merged['billyear'] == dates[X[0]]]

    return [
        dcc.Graph(
            figure=scatter_plot(df=merged),
            style={'width':'inherit', 'height':'inherit'}
        )
    ]


@app.callback(Output('para_coord', 'children'),
             [Input('slider2', 'value')])
def update_figure(X):
    # orderlines = pd.read_csv('/Users/nancy/Downloads/orderlines.txt', sep='\t', encoding='latin-1')
    #
    # products = pd.read_csv('/Users/nancy/Downloads/products.txt', sep='\t', encoding='latin-1')
    #
    # merged_1 = pd.merge(orderlines[['shipdate', 'productid', 'orderid', 'totalprice']],
    #                     products[['PRODUCTID', 'PRODUCTGROUPNAME']],
    #                     left_on='productid', right_on='PRODUCTID',
    #                     how='inner')
    #
    # merged_2 = pd.merge(merged_1, orders[['campaignid', 'orderid']],
    #                     on='orderid', how='inner')
    #
    # merged_2['shipyear'] = pd.to_datetime(merged_2['shipdate']).dt.year
    #
    # merged_3 = pd.merge(merged_2, campaigns[['campaignid', 'freeshippingflag', 'channel']], on='campaignid',
    #                     how='inner')
    #
    # merged_3['log_totalprice'] = np.log(merged_3['totalprice'])
    #
    # merged_4 = merged_3.sample(n=1000, random_state=1)
    #
    # merged_4 = merged_4.sort_values(by='PRODUCTGROUPNAME')

    merged_4 = pd.read_csv('./para_coord.csv')

    merged_4 = merged_4[merged_4['shipyear'] == dates[X[0]]]


    return [
        dcc.Graph(
            figure=para_coord(df=merged_4),
            style={'width':'53vw'}
        )
    ]

@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

if __name__ == "__main__":
    app.run_server(debug=False)
