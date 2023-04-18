import networkx as nx

# read input data from file
with open('data.txt') as f:
    n = int(f.readline().strip())  # number of nodes
    # read adjacency matrix
    adj_matrix = [[int(x) for x in line.strip().split()] for line in f]

# create a graph from the adjacency matrix
G = nx.Graph()
for i in range(n):
    for j in range(i, n):
        if adj_matrix[i][j] > 0:
            G.add_edge(i, j, weight=adj_matrix[i][j])

# find the minimum distance for each pair of nodes
all_pairs = dict(nx.all_pairs_dijkstra_path_length(G))

# initialize the odd vertices list
odd_vertices = [v for v in G.nodes if G.degree(v) % 2 == 1]

# create a complete graph from the odd vertices
complete_graph = nx.Graph()
for i in range(len(odd_vertices)):
    for j in range(i+1, len(odd_vertices)):
        complete_graph.add_edge(odd_vertices[i], odd_vertices[j], weight=all_pairs[odd_vertices[i]][odd_vertices[j]])

# find the minimum weight matching in the complete graph
matching = nx.algorithms.max_weight_matching(complete_graph)

# create a new graph with the matched edges duplicated
for u, v in matching:
    path = all_pairs[u][v]
    for i in range(path):
        G.add_edge(u, v, weight=adj_matrix[u][v])

# find an eulerian circuit in the modified graph
circuit = list(nx.algorithms.eulerian_circuit(G))

# calculate the length of the circuit
length = sum([G[u][v]['weight'] for u, v in circuit])

print("Найкоротший шлях, при якому потрібно пройтися по всім вершинам:", circuit)
print("Довжина шляху:", length)