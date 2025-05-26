import json
import networkx as nx

# Function to process the graph creation
def process_graph(edges_file, nodes_file, multiplex_filename):
    # Load data_WS2425 from JSON files
    with open(edges_file, 'r') as json_file:
        edges_dict = json.load(json_file)

    with open(nodes_file, 'r') as json_file:
        nodes_dict = json.load(json_file)

    # Create the directed multigraph (multiplex) and add edges for each type
    G_multi = nx.MultiDiGraph()
    edge_types = ["aquaintance", "leftright", "sentiment", "friend", "value", "politics", "study", "council"]
    for source, targets in edges_dict.items():
        for target, edge_attributes in targets.items():
            for edge_type in edge_types:
                if edge_type in edge_attributes:
                    if edge_type in ["friend", "value", "politics", "study", "council", "aquaintance"]:
                        if edge_attributes[edge_type]:
                            G_multi.add_edge(source, target, key=edge_type,type=edge_type)
                    elif edge_type == "leftright" and edge_attributes[edge_type] is not None and edge_attributes[edge_type] != 0:
                        G_multi.add_edge(source, target, key=edge_type, type=edge_type, weight=edge_attributes[edge_type])
                    elif edge_type == "sentiment" and edge_attributes[edge_type] is not None:
                        G_multi.add_edge(source, target, key=edge_type, type=edge_type, weight=edge_attributes[edge_type])

    # Add node-specific attributes to the multiplex graph
    for node, attributes in nodes_dict.items():
        G_multi.add_node(node, **attributes)

    # Write the multiplex graph to a GML file
    nx.write_gml(G_multi, multiplex_filename)
    print(f"Multiplex graph '{multiplex_filename}' created with {len(G_multi.nodes)} nodes and {len(G_multi.edges)} edges.")

# Process W2 and W1 datasets
process_graph(
    '/Users/ramius/Desktop/CodeVault/01_Project/Work/Susumu/Student_Survey/StudentSurvey_GitDock/data_WS2425/NA/edges_W1.json',
    '/Users/ramius/Desktop/CodeVault/01_Project/Work/Susumu/Student_Survey/StudentSurvey_GitDock/data_WS2425/NA/nodes_W1.json',
    '/Users/ramius/Desktop/CodeVault/01_Project/Work/Susumu/Student_Survey/StudentSurvey_GitDock/data_WS2425/NA/multiplex_graph_w1.gml'
)

process_graph(
    '/Users/ramius/Desktop/CodeVault/01_Project/Work/Susumu/Student_Survey/StudentSurvey_GitDock/data_WS2425/NA/edges_W2.json',
    '/Users/ramius/Desktop/CodeVault/01_Project/Work/Susumu/Student_Survey/StudentSurvey_GitDock/data_WS2425/NA/nodes_W2.json',
    '/Users/ramius/Desktop/CodeVault/01_Project/Work/Susumu/Student_Survey/StudentSurvey_GitDock/data_WS2425/NA/multiplex_graph_w2.gml'
)

process_graph(
    '/Users/ramius/Desktop/CodeVault/01_Project/Work/Susumu/Student_Survey/StudentSurvey_GitDock/data_WS2425/NA/edges_W3.json',
    '/Users/ramius/Desktop/CodeVault/01_Project/Work/Susumu/Student_Survey/StudentSurvey_GitDock/data_WS2425/NA/nodes_W3.json',
    '/Users/ramius/Desktop/CodeVault/01_Project/Work/Susumu/Student_Survey/StudentSurvey_GitDock/data_WS2425/NA/multiplex_graph_w3.gml'
)
