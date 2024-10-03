import networkx as nx
import urllib.request
import gzip
import io

# Step 1: Load the Facebook combined data
url = 'https://snap.stanford.edu/data/facebook_combined.txt.gz'

# Download and read the compressed file
response = urllib.request.urlopen(url)
compressed_file = io.BytesIO(response.read())

# Open the gzip file
with gzip.GzipFile(fileobj=compressed_file) as f:
    # Create the graph from the edge list
    G = nx.read_edgelist(f, nodetype=int)

# Step 2: Calculate the graph properties
# 1. Average Degree
degrees = [deg for _, deg in G.degree()]
average_degree = sum(degrees) / len(degrees)

# 2. Transitivity (global clustering coefficient)
transitivity = nx.transitivity(G)

# 3. Diameter
if nx.is_connected(G):
    diameter = nx.diameter(G)
else:
    # For disconnected graphs, we compute the diameter of the largest component
    largest_cc = max(nx.connected_components(G), key=len)
    diameter = nx.diameter(G.subgraph(largest_cc))

# 4. Radius
if nx.is_connected(G):
    radius = nx.radius(G)
else:
    radius = nx.radius(G.subgraph(largest_cc))

# Step 3: Print the results
print(f"Average Degree: {average_degree}")
print(f"Transitivity (Global Clustering Coefficient): {transitivity}")
print(f"Diameter: {diameter}")
print(f"Radius: {radius}")
