import sys
import math

def print_debug(msg):
    print("{}".format(msg), file=sys.stderr)

def list_minus_list(list1,list2):
    for value in list2:
        list1.remove(value)
    return list1

def is_critical_situation(escape_paths, node_gates_count):
    for path in escape_paths:
        path_score = len(path)
        for node in path:
            if node in node_gates_count:
                gates_count = node_gates_count[node]
                path_score -= gates_count
        if path_score < 2:
            return True
    return False

class Graph():
    def __init__(self, graph_dict=None):
        """ initializes a graph object
            If no dictionary or None is given, an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict
        self.weights = {}
        self.edges = graph_dict

    def get_nodes(self):
        """ returns the nodes of a graph """
        return list(self.__graph_dict.keys())

    def get_adj_nodes(self, node):
        """ returns the nodes of a graph """
        return list(self.__graph_dict[node])

    def get_edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def get_degree(self, node):
        """ The degree of a vertex is the number of edges connecting
            it, i.e. the number of adjacent vertices. Loops are counted
            double, i.e. every occurence of vertex in the list
            of adjacent vertices. """
        adj_nodes = self.__graph_dict[node]
        degree = len(adj_nodes) + adj_nodes.count(node)
        #print_debug('degree of node({}):{}'.format(node,degree))
        return degree

    def get_degree_sum(self, nodes):
        degree_sum = 0
        for node in nodes:
            degree_sum += self.get_degree(node)
        return degree_sum

    def __generate_edges(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """
        edges = []
        for node in self.__graph_dict:
            for neighbor in self.__graph_dict[node]:
                if {neighbor, node} not in edges:
                    edges.append({node, neighbor})
        return edges

    def __str__(self):
        res = "nodes: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nlinks: "
        for link in self.__generate_links():
            res += str(link) + " "
        return res

    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight

    def del_edge(self, from_node, to_node):
        self.edges[from_node].remove(to_node)
        self.edges[to_node].remove(from_node)

    def add_node(self, node):
        """ If the vertex "vertex" is not in
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if node not in self.__graph_dict:
            self.__graph_dict[node] = []

    def find_path(self, start_node, end_node, path=[]):
        """ find a path from start_node to end_node
            in graph """
        graph = self.__graph_dict
        path = path + [start_node]
        if start_node == end_node:
            return path
        if start_node not in graph:
            return None
        for node in graph[start_node]:
            if node not in path:
                extended_path = self.find_path(node,
                                               end_node,
                                               path)
                if extended_path:
                    return extended_path
        return None

    def find_all_paths(self, start_node, end_node, path=[]):
        """ find all paths from start_node to
            end_node in graph """
        graph = self.__graph_dict
        path = path + [start_node]
        if start_node == end_node:
            return [path]
        if start_node not in graph:
            return []
        paths = []
        for node in graph[start_node]:
            if node not in path:
                extended_paths = self.find_all_paths(node,
                                                     end_node,
                                                     path)
                for p in extended_paths:
                    paths.append(p)
        return paths

    def find_shortest_path(self, start_node, end_node, path=[]):
        graph = self.__graph_dict
        path = path + [start_node]
        if start_node == end_node:
            return path
        if start_node not in graph.keys():
            return None
        shortest = None
        for node in graph[start_node]:
            if node not in path:
                newpath = self.find_shortest_path(node, end_node, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest


    def dijsktra(self, initial, end):
        # whose value is a tuple of (previous node, weight)
        shortest_paths = {initial: (None, 0)}
        current_node = initial
        visited = set()

        while current_node != end:
            visited.add(current_node)
            destinations = self.edges[current_node]
            weight_to_current_node = shortest_paths[current_node][1]

            for next_node in destinations:
                weight = self.weights[(current_node, next_node)] + weight_to_current_node
                if next_node not in shortest_paths:
                    shortest_paths[next_node] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_paths[next_node][1]
                    if current_shortest_weight > weight:
                        shortest_paths[next_node] = (current_node, weight)

            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
            if not next_destinations:
                return "Route Not Possible"
            # next node is the destination with the lowest weight
            current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

        # Work back through destinations in shortest path
        path = []
        while current_node is not None:
            path.append(current_node)
            next_node = shortest_paths[current_node][0]
            current_node = next_node
        # Reverse path
        path = path[::-1]
        return path

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
graph = Graph()

# add empty nodes
for i in range(n):
    graph.add_node(i)

# add edges for each node, current weigh is set to 1
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    weight = 1
    graph.add_edge(n1, n2, weight)

gates = []
# collect the gateway node into gates
for i in range(e):
    ei = int(input())  # the index of a gateway node
    gates.append(ei)
print_debug('gates:{}'.format(gates))
#print_debug('nodes:{}'.format(graph.get_nodes()))

# game loop
count = 1
while True:
    current_node = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    escape_paths = []
    cut_candidates_score_mapping = {}
    direct_node_to_gate = []
    node_gates_count = {}
    multiple_gates_node = {}
    for gate_node in gates:
        # find shortest path to gate
        shortest_path_to_gate = graph.dijsktra(current_node, gate_node)
        print_debug('node({}) to gate({}):{}'.format(current_node, gate_node, shortest_path_to_gate))
        if isinstance(shortest_path_to_gate, list):
            escape_paths.append(shortest_path_to_gate)

        # calculate the degree of all candidate edges
        adj_nodes = graph.get_adj_nodes(gate_node)
        for node in adj_nodes:
            key = (gate_node, node)
            value = graph.get_degree_sum([gate_node,node])
            cut_candidates_score_mapping[key] = value
            # identify the direct_node_to_gate
            if node not in direct_node_to_gate:
                direct_node_to_gate.append(node)

    # identify the direct node connect to mutiple gates
    for node in direct_node_to_gate:
        adj_nodes = graph.get_adj_nodes(node)
        gate_count = 0
        for gate in gates:
            if gate in adj_nodes:
                gate_count += 1
        if gate_count > 1:
            multiple_gates_node[node] = gate_count
        node_gates_count[node] = gate_count

    print_debug('direct_node_to_gate:{}'.format(direct_node_to_gate))
    print_debug('multiple_gates_node:{}'.format(multiple_gates_node))
    # sort according to the value from big to small
    cut_candidates_score_mapping = dict(sorted(cut_candidates_score_mapping.items(), key=lambda x: x[1], reverse=True))
    print_debug('cut_candidates_score_mapping:{}'.format(cut_candidates_score_mapping))

    # find the shortest path between gates
    print_debug('escape paths:{}'.format(escape_paths))
    cut_path = escape_paths[0]
    for path in escape_paths:
        print_debug('working_path:{}'.format(path))
        cut_path_degree = graph.get_degree_sum(cut_path)
        current_path_degree = graph.get_degree_sum(path)
        # use the shortest path first
        if len(path) < len(cut_path):
            print_debug('rule:1')
            cut_path = path
            print_debug('cut_path:{}'.format(cut_path))
        # path length is the same, use the hightest degree
        if len(path) == len(cut_path):
            print_debug('rule:2')
            print_debug('cut_path_degree:{},current_path_degree:{}'.format(cut_path_degree,current_path_degree))
            if current_path_degree > cut_path_degree:
                cut_path = path
                print_debug('cut_path:{}'.format(cut_path))
            if current_path_degree == cut_path_degree:
                print_debug('degree is the same !!!!')

    # not the urgent situation, cut the highest score edge
    if not is_critical_situation(escape_paths, node_gates_count):
        print_debug('rule:4')
        cut_candidate = list(cut_candidates_score_mapping.keys())[0]
        for tmp_cut_candidate, value in cut_candidates_score_mapping.items():
            print_debug('cut_candidate:{},tmp_cut_candidate:{},value:{}'.format(cut_candidate,tmp_cut_candidate,value))
            if value > cut_candidates_score_mapping[cut_candidate]:
                cut_candidate = tmp_cut_candidate
            # degree is the same, check whether there is gate node
            elif value == cut_candidates_score_mapping[cut_candidate]:
                node1,node2 = tmp_cut_candidate
                if node1 in gates or node2 in gates:
                    cut_candidate = tmp_cut_candidate
                elif node1 in multiple_gates_node or node2 in multiple_gates_node:
                    cut_candidate = tmp_cut_candidate
            else:
                continue
        cut_path = list(cut_candidate)
        print_debug('cut_path:{}'.format(cut_path))

    graph.del_edge(cut_path[-2], cut_path[-1])
    print("{} {}".format(cut_path[-2], cut_path[-1]))
    count += 1