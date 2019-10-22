import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Link", href="#")),
        dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            label="Menu",
            children=[
                dbc.DropdownMenuItem("Entry 1"),
                dbc.DropdownMenuItem("Entry 2"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Entry 3"),
            ],
        ),
    ],
    brand="Demo",
    brand_href="#",
    sticky="top",
)

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Heading"),
                        dbc.Card([
                            dbc.CardHeader("Distribution of order total by product group",
                                           style={'color': 'white', 'fontWeight': 'bold',
                                                  'backgroundColor': '#717ECD'}),
                            dbc.CardBody(
                                [
                                    dcc.RangeSlider(
                                        id='my-range-slider',
                                        min=0,
                                        max=20,
                                        step=0.5,
                                        value=[5]
                                    ),
                                    html.Div(id='output-container-range-slider'),
                                    dcc.Graph(figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}
                        )
                                ]
                            ),
                        ], color="light", className='h-100', outline=True),
                        dbc.Button("View details", color="secondary"),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                        html.H2("Graph"),
                    ]
                ),
            ]
        )
    ],
    className="mt-4",
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([navbar, body])


@app.callback(
    dash.dependencies.Output('output-container-range-slider', 'children'),
    [dash.dependencies.Input('my-range-slider', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)


if __name__ == "__main__":
    app.run_server(host='127.0.0.1', port='7000')