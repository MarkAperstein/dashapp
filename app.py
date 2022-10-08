# notes
'''
This file is for housing the main dash application.
This is where we define the various css items to fetch as well as the layout of our application.
'''

# package imports
import dash
from dash import html
import dash_bootstrap_components as dbc


from components import navbar, footer

import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output
import components
import pages

app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])
server=app.server

nav= components.navbar.navbar

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav,
    html.Div(id='page-content', children=[]),
])

# Create the callback to handle mutlipage inputs
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/pages/home':
        return pages.home.layout
    if pathname == '/pages/nowcast':
        return pages.nowcast.layout
    if pathname == '/pages/statistics':
        return pages.statistics.layout
    else: # if redirected to unknown link
        return "404 Page Error! Please choose a link"


if __name__ == "__main__":
    server.run_server(debug=True)
