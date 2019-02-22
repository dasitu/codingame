import sys
import math


def print_debug(msg):
    print("{}".format(msg), file=sys.stderr)


class Graph:
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

    def get_weight(self, from_node, to_node):
        return self.weights[(from_node, to_node)]

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
        for link in self.__generate_edges():
            res += str(link) + " "
        return res

    def add_edge(self, from_node, to_node, weight=1):
        if to_node not in self.edges[from_node]:
            self.edges[from_node].append(to_node)
            self.weights[(from_node, to_node)] = weight

    def del_edge(self, from_node, to_node):
        self.edges[from_node].remove(to_node)
        self.edges[to_node].remove(from_node)

    def add_node(self, node):
        if node not in self.__graph_dict:
            self.__graph_dict[node] = []

    def find_path(self, start_node, end_node, path=None):
        """ find a path from start_node to end_node
            in graph """
        if path is None:
            path = []
        graph = self.__graph_dict
        path = path + [start_node]
        if start_node == end_node:
            return path
        if start_node not in graph:
            return None
        for node in graph[start_node]:
            if node not in path:
                extended_path = self.find_path(node, end_node, path)
                if extended_path:
                    return extended_path
        return None

    def find_all_paths(self, start_node, end_node, path=None):
        """ find all paths from start_node to end_node in graph """
        if path is None:
            path = []
        graph = self.__graph_dict
        path = path + [start_node]
        if start_node == end_node:
            return [path]
        if start_node not in graph:
            return []
        paths = []
        for node in graph[start_node]:
            if node not in path:
                extended_paths = self.find_all_paths(node, end_node, path)
                for p in extended_paths:
                    paths.append(p)
        return paths

    def find_shortest_path(self, start_node, end_node, path=None):
        if path is None:
            path = []
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

    def longest_path_dag(self, initial, end):
        # https://www.geeksforgeeks.org/find-longest-path-directed-acyclic-graph/
        # 1) Initialize dist[] = {NINF, NINF, ….} and dist[s] = 0
        #    where s is the source vertex. Here NINF means negative infinite.
        # 2) Create a toplogical order of all vertices.
        # 3) Do following for every vertex u in topological order.
        # ………..Do following for every adjacent vertex v of u
        # ………………if (dist[v] < dist[u] + weight(u, v))
        # ………………………dist[v] = dist[u] + weight(u, v)

        # step 1
        dist = {key: -1*math.inf for key in self.get_nodes()}
        dist[initial] = 0

        # step 2
        topological_sorted_notes = self.topological_sort()

        # step 3
        for u in topological_sorted_notes:
            adj_nodes = self.__graph_dict[u]
            for v in adj_nodes:
                weight = self.get_weight(u, v)
                if dist[v] < dist[u] + weight:
                    dist[v] = dist[u] + weight

            # already found the needed path, stop
            if u == end:
                break
        return dist[end]

    # A recursive function used by topologicalSort
    def topological_sort_util(self, v, visited, stack):
        # Mark the current node as visited.
        visited[v] = True
        # Recur for all the vertices adjacent to this vertex
        for adj_node in self.__graph_dict[v]:
            if not visited[adj_node]:
                self.topological_sort_util(adj_node, visited, stack)
                # Push current vertex to stack which stores result
        stack.insert(0, v)

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topological_sort(self):
        # Mark all the vertices as not visited
        nodes = self.get_nodes()
        visited = {key: False for key in nodes}
        stack =[]

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for node, v in visited.items():
            if not v:
                self.topological_sort_util(node, visited, stack)
                # Print contents of the stack
        return stack

    def get_total_path_cost(self, path):
        total_cost = 0
        for i in range(len(path)-1):
            start_node = path[i]
            to_node = path[i+1]
            weight = self.get_weight(start_node, to_node)
            total_cost += weight
        return total_cost


graph = Graph()
# Total room number
total_rooms = int(input())

# add empty nodes
for i in range(total_rooms):
    graph.add_node(str(i))

# add exit node
graph.add_node('E')

# add edges for each node, current weigh is set to 1
for i in range(total_rooms):
    room, money, n1, n2 = input().split()
    graph.add_edge(room, n1, int(money))
    graph.add_edge(room, n2, int(money))

# g = Graph()
# # # add empty nodes
# for i in range(6):
#     g.add_node(i)
#
# g.add_edge(5, 2)
# g.add_edge(5, 0)
# g.add_edge(4, 0)
# g.add_edge(4, 1)
# g.add_edge(2, 3)
# g.add_edge(3, 1)

print_debug(graph.edges)
print_debug(graph.weights)

print(graph.longest_path_dag('0', 'E'))
