import networkx as nx
import matplotlib.pyplot as plt

class GraphNode:
    all_nodes = []

    def __init__(self, val):
        self.val = val
        self.neighbors = []
        GraphNode.all_nodes.append(self)

    def add_neighbors(self, neighbors):
        self.neighbors.extend(neighbors)

    def adjacent(self):
        print(f"Neighbors of Node {self.val}: {[neighbor.val for neighbor in self.neighbors]}")

def visualize_graph(node):
    G = nx.Graph()
    _visualize_graph(node, G)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold")
    plt.title("Graph Visualization")
    plt.show()

def _visualize_graph(node, G, visited=None):
    if visited is None:
        visited = set()
    if node in visited:
        return
    visited.add(node)
    for neighbor in node.neighbors:
        G.add_edge(node.val, neighbor.val)
        _visualize_graph(neighbor, G, visited)

# Create a more complicated graph with add_neighbors method
node1 = GraphNode(1)
node2 = GraphNode(2)
node3 = GraphNode(3)
node4 = GraphNode(4)
node5 = GraphNode(5)
node6 = GraphNode(6)
node7 = GraphNode(7)
node8 = GraphNode(8)

# Adding neighbors using the add_neighbors method
node1.add_neighbors([node2, node3, node7])
node2.add_neighbors([node1, node4, node5, node8])
node3.add_neighbors([node1, node6])
node4.add_neighbors([node2])
node5.add_neighbors([node2, node7])
node6.add_neighbors([node3, node8])
node7.add_neighbors([node5])
node8.add_neighbors([node6])

print([x.val for x in GraphNode.all_nodes[1].neighbors])


# Visualize the graph
visualize_graph(node1)


print(GraphNode.all_nodes[5].neighbors[0].val)

def color_finder(GraphNode):
    for node in GraphNode.all_nodes:
        neighbors_sum = sum(neighbor.val for neighbor in node.neighbors)
        print(f"Sum of neighbors of Node {node.val}: {neighbors_sum}")

# Example usage
color_finder(GraphNode)
