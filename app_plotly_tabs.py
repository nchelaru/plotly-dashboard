import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from graphs import *
from dash.dependencies import Input, Output, State
from datetime import date


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


orders_df = orders_data()

jumbotron = dbc.Jumbotron(
    [
        html.H2("Sales dashboard", className="display-3"),
        html.P(datetime.datetime.now().strftime("%A, %B %d %Y"),
            className="lead",
        ),
    ]
)

sales_layout = html.Div([
    html.Div(
        className='row',
        children=[
            html.Div(
                className='four columns',
                children=dcc.Graph(
                    id='one-gauge',
                    figure=gauge(),
                    style={'height':'20vh'}),
                ),
            html.Div(
                className='four columns',
                children=dcc.Graph(
                    id='two-gauge',
                    figure=gauge(),
                    style={'height':'20vh'}),
                ),
            html.Div(
                className='four columns',
                children=dcc.Graph(
                    id='three-gauge',
                    figure=gauge(),
                    style={'height':'20vh'}),
                )
        ], style={'height':'10vh'}
    ),
    html.Div(
        className='row',
        children=[
            html.Div(
                className='five columns',
                children=[
                    html.Div(
                        children=dcc.Graph(
                            id='bullet-chart',
                            figure=bullet_chart(),
                            style={'height': '60vh'}
                        )
                    )], style={'height': '60vh'}
            ),
            html.Div(
                className='seven columns',
                children=dash_table.DataTable(
                            id='table-sorting-filtering',
                            columns=[
                                {'name': i, 'id': i, 'deletable': True} for i in orders_df.columns
                            ],
                            style_table={'overflowX': 'scroll'},
                            style_data_conditional=[
                                    {
                                        'if': {'row_index': 'odd'},
                                        'backgroundColor': 'rgb(248, 248, 248)'
                                    }
                                ],
                            style_cell={
                                    'height': 'auto',
                                    'minWidth': '80px',
                                },
                            page_current= 0,
                            page_size= 15,
                            page_action='custom',
                            filter_action='custom',
                            filter_query='',
                            sort_action='custom',
                            sort_mode='multi',
                            sort_by=[]
                        ),
                style={'height': '60vh'}
            )
        ], style={'height': '60vh'}
    ),
    html.Div(
        className="row",
        children=[
            html.Div(
                className="five columns",
                children=dcc.Graph(
                    id='left-graph',
                    figure=sales_map(),
                    style={'height':'60vh'})
                    ),
            html.Div(
                className="seven columns",
                children=dcc.Graph(
                    id='right-top-graph',
                    figure=sales_timeline(),
                    style={'height': '70vh'}
                ),
            )
                ], style={'height':'60vh'}
            ),
        ], style={'height': '60vh'}
    )





app.layout = html.Div([
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='Sales', children=[
            sales_layout
        ], style={'padding':'8px', 'fontWeight': 'bold'}),
        dcc.Tab(label='Products', children=[
                dcc.Graph(
                    id='example-graph-1',
                    figure=gauge()
                )
        ], style={'padding':'8px', 'fontWeight': 'bold'}),
        dcc.Tab(label='Campaigns', children=[
            dbc.Row([
                    dbc.Col(dcc.Graph(figure=gauge()), width=6),
                    dbc.Col(dcc.Graph(figure=gauge()), width=6)
                ]),
            dbc.Row(
                    dbc.Col(dbc.Card(dcc.Graph(figure=gauge())), width=12)
                )
        ], style={'padding':'8px', 'fontWeight': 'bold'})
    ], style={'height':'50px'})
], style={'margin':'20px'})



@app.callback(
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




if __name__ == '__main__':
    app.run_server(debug=True)