# Shortest Path Finding in OpenStreetMap Data

## Overview
This project implements a shortest path finding algorithm using OpenStreetMap (OSM) data. It allows users to compute the most efficient route between two points based on real-world map data.

## Features
- Parses OpenStreetMap (OSM) data to extract road networks.
- Implements shortest path algorithms such as Dijkstra's and A*.
- Supports multiple routing criteria such as distance and travel time.
- Provides visualization of the computed route.
- Can handle large-scale OSM datasets.

## Requirements
- Python 3.x
- Required Python libraries:
  - `osmnx`
  - `networkx`
  - `matplotlib`
  - `geopy`
    

To install dependencies, run:
```sh
pip install -r requirements.txt
```

## Usage
### 1. Download OSM Data
You can download OpenStreetMap data using the `osmnx` library:
```python
import osmnx as ox
import networkx as nx

# Define location (Nepal) and transport mode (driving, walking, biking)
place_name = "Kathmandu Nepal"
G = ox.graph_from_place(place_name, network_type="drive")
```

### 2. Find the Shortest Path
```python
import networkx as nx
start_node = 1127867287
end_node = 1924770845

# Check if nodes exist in the graph
if start_node not in place or end_node not in place:
    raise ValueError("One or both node IDs are not in the graph!")

# Step 3: Find the shortest path between them
try:
    route = nx.shortest_path(place, source=start_node, target=end_node, weight="length")
except nx.NetworkXNoPath:
    raise ValueError("No path found between the given nodes!")

# Step 4: Plot the graph with the highlighted route
fig, ax = ox.plot_graph_routes(place, [route], route_colors=["red"], route_linewidth=5, node_size=0, show=False, close=False)

# Display the plot
plt.show()
```

### 3. Running the Application
To run the shortest path finder as a script, execute:
```sh
python shortest_path.ipynb
```

## Dataset
The OSM data can be downloaded from:
- [OpenStreetMap](https://www.openstreetmap.org/)
- [Geofabrik](https://download.geofabrik.de/)

## Future Improvements
- Add support for real-time traffic data.
- Implement an interactive web interface.
- Support multiple transportation modes (walking, cycling, public transit).

## License
This project is licensed under the MIT License.


