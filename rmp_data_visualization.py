import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd


from flask import Flask
from plotly import graph_objs as go
from plotly.graph_objs import *


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)
server = app.server

us_cities = pd.read_csv('https://raw.githubusercontent.com/yunerliu/ailabserver/master/newoutcome.csv', encoding='ISO-8859-1', error_bad_lines=False)
all_data = pd.read_csv('https://raw.githubusercontent.com/yunerliu/ailabserver/master/bigdata1.csv',low_memory=False,encoding='ISO-8859-1', error_bad_lines=False)


state_list = {        
"USA":{"lat":37,"lon":-100},
"AL":{"lat":32.806671,"lon":-86.79113},
"AK":{"lat":61.370716,"lon":-152.404419},
"AZ":{"lat":33.729759,"lon":-111.431221},
"AR":{"lat":34.969704,"lon":-92.373123},
"CA":{"lat":36.116203,"lon":-119.681564},
"CO":{"lat":39.059811,"lon":-105.311104},
"CT":{"lat":41.597782,"lon":-72.755371},
"DE":{"lat":39.318523,"lon":-75.507141},
"DC":{"lat":38.897438,"lon":-77.026817},
"FL":{"lat":27.766279,"lon":-81.686783},
"GA":{"lat":33.040619,"lon":-83.643074},
"HI":{"lat":21.094318,"lon":-157.498337},
"ID":{"lat":44.240459,"lon":-114.478828},
"IL":{"lat":40.349457,"lon":-88.986137},
"IN":{"lat":39.849426,"lon":-86.258278},
"IA":{"lat":42.011539,"lon":-93.210526},
"KS":{"lat":38.5266,"lon":-96.726486},
"KY":{"lat":37.66814,"lon":-84.670067},
"LA":{"lat":31.169546,"lon":-91.867805},
"ME":{"lat":44.693947,"lon":-69.381927},
"MD":{"lat":39.063946,"lon":-76.802101},
"MA":{"lat":42.230171,"lon":-71.530106},
"MI":{"lat":43.326618,"lon":-84.536095},
"MN":{"lat":45.694454,"lon":-93.900192},
"MS":{"lat":32.741646,"lon":-89.678696},
"MO":{"lat":38.456085,"lon":-92.288368},
"MT":{"lat":46.921925,"lon":-110.454353},
"NE":{"lat":41.12537,"lon":-98.268082},
"NV":{"lat":38.313515,"lon":-117.055374},
"NH":{"lat":43.452492,"lon":-71.563896},
"NJ":{"lat":40.298904,"lon":-74.521011},
"NM":{"lat":34.840515,"lon":-106.248482},
"NY":{"lat":42.165726,"lon":-74.948051},
"NC":{"lat":35.630066,"lon":-79.806419},
"ND":{"lat":47.528912,"lon":-99.784012},
"OH":{"lat":40.388783,"lon":-82.764915},
"OK":{"lat":35.565342,"lon":-96.928917},
"OR":{"lat":44.572021,"lon":-122.070938},
"PA":{"lat":40.590752,"lon":-77.209755},
"RI":{"lat":41.680893,"lon":-71.51178},
"SC":{"lat":33.856892,"lon":-80.945007},
"SD":{"lat":44.299782,"lon":-99.438828},
"TN":{"lat":35.747845,"lon":-86.692345},
"TX":{"lat":31.054487,"lon":-97.563461},
"UT":{"lat":40.150032,"lon":-111.862434},
"VT":{"lat":44.045876,"lon":-72.710686},
"VA":{"lat":37.769337,"lon":-78.169968},
"WA":{"lat":47.400902,"lon":-121.490494},
"WV":{"lat":38.491226,"lon":-80.954453},
"WI":{"lat":44.268543,"lon":-89.616508},
"WY":{"lat":42.755966,"lon":-107.30249}
        }



app.layout = html.Div([           
    html.Div([
        html.Div([
            html.Div([
                dcc.Markdown(
                    '''
                    ***
                    '''),

                  html.H1(["Rate My Professor Data Visualization"],
                    style = {
                    'margin':'40',
                    'textAlign': 'center',  
                    'color':'#FFFFFF',
                    'display': 'inline-block'
                    }),

            html.Div([
                dcc.Markdown(
                '''
            The picture shows how professor scores distributed in different locations. 
            Here is the [data](http://commonmark.org/help) and the [source code](http://commonmark.org/help)
            ***
                ''')], 
                style={
                    'textAlign': 'center',  
                    'color':'#7FDBFF',
                    }),

            html.Div([
                html.H2(["See Specific"],style={'textAlign': 'center'}),
                html.H4("Choose the state to see local statistics"),
                ],style={
                'textAlign': 'center',  
                'color':'#FFFFFF',
        }),

                dcc.Dropdown(
                    id = 'district',
                    
                    options=[
                    {'label':'unselected','value':'USA'},
                    {'label':'Alabama','value':'AL'},
                    {'label':'Alaska','value':'AK'},
                    {'label':'Arizona','value':'AZ'},
                    {'label':'Arkansas','value':'AR'},
                    {'label':'California','value':'CA'},
                    {'label':'Colorado','value':'CO'},
                    {'label':'Connecticut','value':'CT'},
                    {'label':'Delaware','value':'DE'},
                    {'label':'District of Columbia','value':'DC'},
                    {'label':'Florida','value':'FL'},
                    {'label':'Georgia','value':'GA'},
                    {'label':'Hawaii','value':'HI'},
                    {'label':'Idaho','value':'ID'},
                    {'label':'Illinois','value':'IL'},
                    {'label':'Indiana','value':'IN'},
                    {'label':'Iowa','value':'IA'},
                    {'label':'Kansas','value':'KS'},
                    {'label':'Kentucky','value':'KY'},
                    {'label':'Louisiana','value':'LA'},
                    {'label':'Maine','value':'ME'},
                    {'label':'Maryland','value':'MD'},
                    {'label':'Massachusetts','value':'MA'},
                    {'label':'Michigan','value':'MI'},
                    {'label':'Minnesota','value':'MN'},
                    {'label':'Mississippi','value':'MS'},
                    {'label':'Missouri','value':'MO'},
                    {'label':'Montana','value':'MT'},
                    {'label':'Nebraska','value':'NE'},
                    {'label':'Nevada','value':'NV'},
                    {'label':'New Hampshire','value':'NH'},
                    {'label':'New Jersey','value':'NJ'},
                    {'label':'New Mexico','value':'NM'},
                    {'label':'New York','value':'NY'},
                    {'label':'North Carolina','value':'NC'},
                    {'label':'North Dakota','value':'ND'},
                    {'label':'Ohio','value':'OH'},
                    {'label':'Oklahoma','value':'OK'},
                    {'label':'Oregon','value':'OR'},
                    {'label':'Pennsylvania','value':'PA'},
                    {'label':'Rhode Island','value':'RI'},
                    {'label':'South Carolina','value':'SC'},
                    {'label':'South Dakota','value':'SD'},
                    {'label':'Tennessee','value':'TN'},
                    {'label':'Texas','value':'TX'},
                    {'label':'Utah','value':'UT'},
                    {'label':'Vermont','value':'VT'},
                    {'label':'Virginia','value':'VA'},
                    {'label':'Washington','value':'WA'},
                    {'label':'West Virginia','value':'WV'},
                    {'label':'Wisconsin','value':'WI'},
                    {'label':'Wyoming','value':'WY'}
                    ],
                    value='USA',
                    ),

            html.Div([
                html.H4("Explanation"),
                html.P("The left graph demonstrates the relation between average score and locations in each state."),
                html.P("The right graph demonstrates the relation between average score and professors in each state."),
                ],style={
                'textAlign': 'center',  
                'color':'#FFFFFF',
                'display': 'inline-block',
                    }),
                  ]),
                ],style={'marginBottom': 50,
                        'padding':'30px',
                        'backgroundColor':'#01344E'}),

        html.Div([
            html.Img(id="logo", src=app.get_asset_url("logo.png")),
            ],style={'autosize':True,
                    'marginTop': 100,
                    'backgroundColor':'white'})
            ],
            style={'marginBottom': 50, 
            'marginTop': 25,
            'marginLeft': 25,
            'padding':'30px',
            'width': '25%',
            'display': 'inline-block'}),



    html.Div([
        html.Div([
        dcc.Graph(
            id='life-exp-vs-gdp1', 
            )],style={
                'padding':'15px'   
                }),


        html.Div([
            html.Div([
                dcc.Graph(
                    id='life-exp-vs-gdp2', )
                    ],style={'width': '44%',
                        'padding':'15px',
                        'float': 'left',
                        'display': 'inline-block'}),

        html.Div([
            dcc.Graph(
                id='graph2', 
                )
            ],style={'width': '44%',
            'padding':'15px',
            'float': 'right',
            'display': 'inline-block'}),
        ]),

    ],style={'width': '68%',
    'float': 'right',
    'display': 'inline-block'}),
])




@app.callback(
    dash.dependencies.Output('life-exp-vs-gdp1', 'figure'),
    [dash.dependencies.Input('district', 'value')]
    
)

def update_graph(input_value):
    if input_value == "USA":
        zoom = 3.5
        size = 6
    else:
        zoom = 5.5
        size = 9
    latInitial = state_list[input_value]["lat"]
    lonInitial = state_list[input_value]["lon"]

    return go.Figure(
        data = [
        Scattermapbox(
            lat=us_cities["lat"],
            lon=us_cities["lon"],
            mode='markers',
            marker_color=us_cities["average_score"],
            marker=dict(
                showscale=True,
                opacity=0.5,
                size=size,
                colorscale=[
                [0, "#F4EC15"],
                [0.04167, "#DAF017"],
                [0.0833, "#BBEC19"],
                [0.125, "#9DE81B"],
                [0.1667, "#80E41D"],
                [0.2083, "#66E01F"],
                [0.25, "#4CDC20"],
                [0.292, "#34D822"],
                [0.333, "#24D249"],
                [0.375, "#25D042"],
                [0.4167, "#26CC58"],
                [0.4583, "#28C86D"],
                [0.50, "#29C481"],
                [0.54167, "#2AC093"],
                [0.5833, "#2BBCA4"],
                [1.0, "#613099"],
                ],
                colorbar=dict(
                    title="Average Score",
                    x=1,
                    xpad=0,
                    nticks=24,
                    tickfont=dict(color="#d8d8d8"),
                    titlefont=dict(color="#d8d8d8"),
                    thicknessmode="pixels",
                    ),
                ),
            text=us_cities['average_score'], 
            )
        ],
        layout = Layout(
           height = 800,
           paper_bgcolor="#01344E",
           margin=go.layout.Margin(l=20, r=20, t=20, b=20),
           plot_bgcolor = "#01344E",
           autosize=True,
           hovermode='closest',
           mapbox=dict(
        bearing=0,
        style="dark",
        center=dict(
            lat=latInitial,
            lon=lonInitial,
            ),
        pitch=0,
        zoom=zoom,
        ),
           mapbox_style="open-street-map",
        )
        )


@app.callback(
   dash.dependencies.Output('life-exp-vs-gdp2', 'figure'),
    [dash.dependencies.Input('district', 'value')]
    )
    
def update_graph_score(district):
    alist=[]
    if district.strip() == "USA":
        for row in us_cities.iterrows():
            alist.append(row[1][2])
    else:
        for row in us_cities.iterrows():
            if row[1][1].strip() == district:
                alist.append(row[1][2])
    
    count0 = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    
    for num in alist:
        if num<= 1:
            count0 += 1
        elif num<=2:
            count1 += 1
        elif num<=3:
            count2 += 1
        elif num<=4:
            count3 += 1
        else:
            count4 += 1
    
    blist=[count0,count1,count2,count3,count4]
    
    return go.Figure(
            data=[
                go.Bar(
                    x=[0,1,2,3,4,5],
                    y=blist,
                    name='Location Number',
                    marker=go.bar.Marker(
                        color='rgb(55, 83, 109)'
                    )
                )
             
            ],
            layout=go.Layout(
                      bargap=0.01,
         height = 500,              
        bargroupgap=0,
        barmode="group",
        margin=go.layout.Margin(l=30, r=30, t=40, b=30),
        paper_bgcolor="#01344E",
        plot_bgcolor="#1f2630",
        autosize=True,
        dragmode="select",
        font=dict(color="white"),
                title='graph of average score (based on locations)',
                showlegend=True,
                legend=go.layout.Legend(
                    x=0,
                    y=1.0
                ),
            )
        )
    

@app.callback(
   dash.dependencies.Output('graph2', 'figure'),
    [dash.dependencies.Input('district', 'value')]
    )
    
def update_graph_score(district):
    result = []
    if district == "USA":
        result = [4027,45570,160464,312817,456415]
    else:
        for row in all_data.iterrows():
            if row[1][5] == district:            
                result.append(row[1][0])
                result.append(row[1][1])
                result.append(row[1][2])
                result.append(row[1][3])
                result.append(row[1][4])


    return go.Figure(
            data=[
                go.Bar(
                    x=[0,1,2,3,4,5],
                    y=result,
                    name='Professor Number',
                    marker=go.bar.Marker(
                        color='rgb(55, 83, 109)'
                    )
                )
             
            ],
            layout=go.Layout(
                      bargap=0.01,
        height = 500,                
        bargroupgap=0,
        barmode="group",
        margin=go.layout.Margin(l=30, r=30, t=40, b=30),
        paper_bgcolor="#01344E",
        plot_bgcolor="#1f2630",
        autosize = True,
        dragmode="select",
        font=dict(color="white"),
                title='graph of average score(based on professors)',
                showlegend=True,
                legend=go.layout.Legend(
                    x=0,
                    y=1.0
                ),
            )
        )    




if __name__ == '__main__':
    app.run_server(debug=True)
