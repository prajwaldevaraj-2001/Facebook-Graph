# Facebook Graph

This project implements a **Facebook Graph** model using network analysis techniques. It leverages graph theory to model and analyze the connections and interactions between users on a social network, representing them as a graph where nodes are users and edges are the relationships or interactions between them.

📂 **GitHub Repository:** [Facebook Graph](https://github.com/prajwaldevaraj-2001/Facebook-Graph)

---

## 🚀 Overview

The **Facebook Graph** model focuses on exploring and analyzing social networks by constructing a graph representation of the user interactions. This system models users as nodes and their interactions (e.g., friendship, messages, likes) as edges. Various graph algorithms are then applied to analyze the structure and behavior of the network.

### 🔹 Key Features:
- **Graph Construction**: Builds a graph based on user interactions like friend requests, messages, and likes.
- **Graph Algorithms**: Implements algorithms like **Breadth-First Search (BFS)**, **Depth-First Search (DFS)**, **Shortest Path**, and **Centrality Analysis**.
- **Visualization**: Visualizes the social network graph to identify key users, communities, and interaction patterns.
- **Community Detection**: Identifies groups of users who are closely connected within the network.
- **Network Analysis**: Analyzes network properties such as degree distribution, clustering coefficients, and connected components.

---

## 🛠️ Technologies Used

- **Python**: Primary language for implementation.
- **NetworkX**: Python library for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
- **Matplotlib**: For visualizing the network graphs.
- **Pandas**: For data manipulation and processing.
- **NumPy**: For numerical operations.

---

## ⚙️ Installation & Setup
🔹 1. Clone the Repository</br>
git clone https://github.com/prajwaldevaraj-2001/Facebook-Graph.git</br>
cd Facebook-Graph</br>

🔹 2. Install Dependencies</br>
Install the required libraries:</br>
pip install -r requirements.txt</br>

## 🔧 Usage
🔹 1. Load Data</br>
Ensure you have the social network interaction data file (facebook_data.csv). The data should contain information like users and their connections (e.g., friends, messages). Load this data into the system for further analysis.</br>

🔹 2. Graph Construction</br>
Use the script main.py to construct the graph from the interaction data:</br>
python main.py</br>

🔹 3. Run Graph Algorithms</br>
Run various graph algorithms to analyze the network:</br>
Breadth-First Search (BFS):</br>
python algorithms/bfs.py</br>
Depth-First Search (DFS):</br>
python algorithms/dfs.py</br>
Centrality Analysis (e.g., degree centrality, closeness centrality, betweenness centrality):</br>
python algorithms/centrality.py</br>
Community Detection (using algorithms like modularity maximization):</br>
python algorithms/community_detection.py</br>

🔹 4. Visualize the Network</br>
You can visualize the constructed graph using the following scripts:</br>
Plot Graph:</br>
python visualization/plot_graph.py</br>
Plot Communities (if community detection is applied):</br>
python visualization/plot_community.py</br>

## 📊 Example Usage
Load Data:</br>
Prepare the dataset and load it into the system to generate a network graph.</br>
python main.py</br>

Run BFS/DFS:</br>
Perform Breadth-First Search or Depth-First Search to explore the graph.</br>
python algorithms/bfs.py</br>
python algorithms/dfs.py</br>

Centrality Analysis:</br>
Run centrality algorithms to identify the most important nodes in the network:</br>
python algorithms/centrality.py</br>

Community Detection:</br>
Detect communities within the network to identify tightly-knit groups of users:</br>
python algorithms/community_detection.py</br>

Visualize the Graph:</br>
Visualize the graph or communities for better insight into the network structure:</br>
python visualization/plot_graph.py</br>
python visualization/plot_community.py</br>

## Future Improvements
- ✅ Real-time Network Analysis: Implement real-time data processing to analyze new interactions as they occur.
- ✅ Advanced Community Detection: Explore more sophisticated community detection algorithms like Louvain and Girvan-Newman.
- ✅ Network Evolution: Study how the social network evolves over time and how user behavior changes.

## 📂 Project Structure

```plaintext
Facebook-Graph/
│
├── data/                          # Dataset and related files
│   ├── facebook_data.csv          # Social network interaction data (user, friend, etc.)
│
├── algorithms/                    # Graph algorithms
│   ├── bfs.py                     # Breadth-First Search
│   ├── dfs.py                     # Depth-First Search
│   ├── centrality.py              # Centrality analysis
│   ├── community_detection.py     # Community detection
│
├── visualization/                 # Graph visualization
│   ├── plot_graph.py              # Script to visualize the social graph
│   ├── plot_community.py          # Visualize communities
│
├── requirements.txt               # Python dependencies
├── README.md                      # Documentation
└── main.py                         # Main entry point for running the project
