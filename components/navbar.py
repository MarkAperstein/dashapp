from dash import html
import dash_bootstrap_components as dbc

def Navbar():

    layout = html.Div([
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Home", href="/pages/home")),
                dbc.NavItem(dbc.NavLink("Real-time Data", href="/pages/nowcast")),
                dbc.NavItem(dbc.NavLink("Statistics",href="/pages/statistics"))
            ] ,
            brand="IDF Navy Met-Oc App",
            brand_href="/home",
            color="dark",
            dark=True,
        ), 
    ])

    return layout

navbar=Navbar()