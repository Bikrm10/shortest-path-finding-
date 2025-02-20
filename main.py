import osmnx as ox
import folium
import networkx as nx

# # Define the location (Kathmandu, Nepal)
# place_name = "Kathmandu, Nepal"

# # Get the graph (you can choose 'all', 'walk', 'bike', or 'drive')
# graph = ox.graph_from_place(place_name, network_type="drive")

# # Get nodes (coordinates) and edges
# nodes, edges = ox.graph_to_gdfs(graph)

# # Create a folium map centered around Kathmandu
# map_center = [nodes['y'].mean(), nodes['x'].mean()]
# m = folium.Map(location=map_center, zoom_start=12, tiles="cartodbpositron")

# # Plot nodes (intersections/points)
# for _, node in nodes.iterrows():
#     folium.CircleMarker(
#         location=[node['y'], node['x']],
#         radius=1,  # Small size for better visibility
#         color="red",
#         fill=True,
#         fill_color="red",
#         fill_opacity=0.6,
#     ).add_to(m)

# # Plot edges (roads)
# for _, edge in edges.iterrows():
#     if isinstance(edge["geometry"], list):
#         continue
#     locations = [(lat, lon) for lon, lat in edge["geometry"].coords]
#     folium.PolyLine(locations, color="blue", weight=1, opacity=0.7).add_to(m)

# # Save map as an HTML file
# m.save("kathmandu_road_network.html")

# # Display map in a Jupyter Notebook (optional)

import networkx as nx

# Create a graph
G = nx.Graph()
G.add_weighted_edges_from([
    ('A', 'B', 4), ('A', 'C', 2), ('B', 'C', 1),
    ('B', 'D', 5), ('C', 'D', 8), ('D', 'E', 3)
])

# Find the shortest path from 'A' to 'E'
shortest_path = nx.dijkstra_path(G, source='A', target='E', weight='weight')
print("Shortest Path:", shortest_path)

#astar heuristic
def heuristic(u, v):
    """Example heuristic function (assuming coordinates are available)."""
    return abs(ord(u) - ord(v))
path = nx.astar_path(G, source='A', target='E', weight='weight', heuristic=heuristic)
print("A* Path:", path)