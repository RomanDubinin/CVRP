import plotly
from plotly.graph_objs import Scatter3d, Layout, Marker, Line, Scene, XAxis, YAxis, ZAxis, Margin, Annotation

my_scale = ["#FF0000",
            "#FF00CD",
            "#9500FF",
            "#3300FF",
            "#0095FF",
            "#00FFE6",
            "#00FF11",
            "#FFF700",
            "#FF6F00",
            "#66EBA8",
            "#000000",
            "#6994BF",]

def experimental_antibug_visualize(depo_nodes, customer_nodes, edges):
    traces = []
    for i in range(len(depo_nodes)):
        traces.append(Scatter3d(x=[depo_nodes[i]["coords"][0]],
                                y=[depo_nodes[i]["coords"][1]],
                                z=[depo_nodes[i]["coords"][2]],
                                mode='markers',
                                name='depos',
                                marker=Marker(symbol='dot',
                                              size=12,
                                              color=my_scale[depo_nodes[i]["group"]],
                                              line=Line(color='rgb(50,50,50)', width=0.5)
                                              ),
                                text=depo_nodes[i]["name"],
                                hoverinfo='text'
                           ))

    for i in range(len(customer_nodes)):
        traces.append(Scatter3d(x=[customer_nodes[i]["coords"][0]],
                                y=[customer_nodes[i]["coords"][1]],
                                z=[customer_nodes[i]["coords"][2]],
                                mode='markers',
                                name='customers',
                                marker=Marker(symbol='dot',
                                             size=6,
                                             color=my_scale[customer_nodes[i]["group"]],
                                             line=Line(color='rgb(50,50,50)', width=0.5)
                                             ),
                                text=customer_nodes[i]["name"],
                                hoverinfo='text'
                                ))

    xe = []
    ye = []
    ze = []
    for e in edges:
        xe += [e["source"][0], e["target"][0], None]  # x-coordinates of edge ends
        ye += [e["source"][1], e["target"][1], None]
        ze += [e["source"][2], e["target"][2], None]

    traces.append(Scatter3d(x=xe,
                            y=ye,
                            z=ze,
                            mode='lines',
                            line=Line(color='rgb(125,0,125)', width=5),
                            hoverinfo='text'
                            ))

    axis = dict(showbackground=True,
                showline=True,
                zeroline=False,
                showgrid=True,
                showticklabels=True,
                title=''
                )

    layout = Layout(
        title="Network of ...",
        width=1200,
        height=800,
        showlegend=False,
        scene=Scene(
            xaxis=XAxis(axis),
            yaxis=YAxis(axis),
            zaxis=ZAxis(axis),
        ),
        margin=Margin(
            t=100
        ),
        hovermode='closest')

    plotly.offline.plot({
        "data": traces,
        "layout": layout
    })

def visualize(depo_nodes, customer_nodes, edges):
    customers_count = len(customer_nodes)
    depo_count = len(depo_nodes)


    print(edges)

    customer_labels = []
    customer_group = []
    for node in customer_nodes:
        customer_labels.append(node['name'])
        customer_group.append(node['group'])

    depo_labels = []
    depo_group = []
    for node in depo_nodes:
        depo_labels.append(node['name'])
        depo_group.append(node['group'])

    customer_x = [customer_nodes[k]["coords"][0] for k in range(customers_count)]  # x-coordinates of nodes
    customer_y = [customer_nodes[k]["coords"][1] for k in range(customers_count)]  # y-coordinates
    customer_z = [customer_nodes[k]["coords"][2] for k in range(customers_count)]  # z-coordinates

    depo_x = [depo_nodes[k]["coords"][0] for k in range(depo_count)]  # x-coordinates of nodes
    depo_y = [depo_nodes[k]["coords"][1] for k in range(depo_count)]  # y-coordinates
    depo_z = [depo_nodes[k]["coords"][2] for k in range(depo_count)]  # z-coordinates

    xe = []
    ye = []
    ze = []
    for e in edges:
        xe += [e["source"][0], e["target"][0], None]  # x-coordinates of edge ends
        ye += [e["source"][1], e["target"][1], None]
        ze += [e["source"][2], e["target"][2], None]

    trace1 = Scatter3d(x=xe,
                       y=ye,
                       z=ze,
                       mode='lines',
                       line=Line(color='rgb(125,0,125)', width=5),
                       hoverinfo='text'
                       )
    trace2 = Scatter3d(x=customer_x,
                       y=customer_y,
                       z=customer_z,
                       mode='markers',
                       name='customers',
                       marker=Marker(symbol='dot',
                                     size=6,
                                     color=[2,0],
                                     colorscale='Viridis',
                                     line=Line(color='rgb(50,50,50)', width=0.5)
                                     ),
                       text=customer_labels,
                       hoverinfo='text'
                       )

    trace3 = Scatter3d(x=depo_x,
                       y=depo_y,
                       z=depo_z,
                       mode='markers',
                       name='depos',
                       marker=Marker(symbol='dot',
                                     size=12,
                                     color=[0,1,2],
                                     colorscale='Viridis',
                                     line=Line(color='rgb(50,50,50)', width=0.5)
                                     ),
                       text=depo_labels,
                       hoverinfo='text'
                       )
    axis = dict(showbackground=True,
                showline=True,
                zeroline=False,
                showgrid=True,
                showticklabels=True,
                title=''
                )

    layout = Layout(
        title="Network of ...",
        width=1200,
        height=800,
        showlegend=True,
        scene=Scene(
            xaxis=XAxis(axis),
            yaxis=YAxis(axis),
            zaxis=ZAxis(axis),
        ),
        margin=Margin(
            t=100
        ),
        hovermode='closest')


    plotly.offline.plot({
        "data": [trace1, trace2, trace3],
        "layout": layout
    })
