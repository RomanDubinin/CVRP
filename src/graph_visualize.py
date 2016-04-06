import plotly
from plotly.graph_objs import Scatter3d, Layout, Marker, Line, Scene, XAxis, YAxis, ZAxis, Margin, Annotation


def visualize(depo_nodes, customer_nodes, edges):
    customers_count = len(customer_nodes)
    depo_count = len(depo_nodes)

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

    print(depo_group)
    print(customer_group)

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
                       line=Line(color='rgb(125,125,125)', width=1),
                       hoverinfo='text'
                       )
    trace2 = Scatter3d(x=customer_x,
                       y=customer_y,
                       z=customer_z,
                       mode='markers',
                       name='customers',
                       marker=Marker(symbol='dot',
                                     size=6,
                                     color=customer_group,
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
                                     color=depo_group,
                                     colorscale='Viridis',
                                     line=Line(color='rgb(50,50,50)', width=0.5)
                                     ),
                       text=depo_labels,
                       hoverinfo='text'
                       )

    layout = Layout(
        title="Network of ...",
        width=1200,
        height=800,
        showlegend=True,
        scene=Scene(

        ),
        margin=Margin(
            t=100
        ),
        hovermode='closest')

    plotly.offline.plot({
        "data": [trace1, trace2, trace3],
        "layout": layout
    })
