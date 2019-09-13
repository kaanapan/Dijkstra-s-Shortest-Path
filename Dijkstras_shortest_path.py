class Solver:
    def __init__(self,n_nodes,start_node):
        """
        :param n_nodes: number of nodes
        :param start_node: starting node for Dijkstra's shortest Path
        :param self.X : Nodes that are processed
        :param self.A : Dictionary that holds the shortest path for processed nodes
        :param self.adj_list : Adjacency list list representation of Graph
        """
        self.X = {start_node}
        self.n = n_nodes
        self.A = {start_node:0}
        self.adj_list = [[] for _ in range(n_nodes+1)]
    def load_file(self, file_name, delimeter_edges, delimeter_weight):
        """
        :param file_name: Name of the file that carries Adjacency list representation.
        :param delimeter_edges: Delimeter that seperates edges, end of the line also should include this
        :param delimeter_weight: Delimeter that seperates heads and weights
        File's format is following:

        1       25.251      95.512      159.2341
        2       21.234
        3
        4       51.4        423.1
        ^       ^^ ^
        <tail>  <head>.<weight>
        :return: Nothing
        """
        file = open(file_name)
        node_counter = 1
        for line in file:
            line_processed = line.split(delimeter_edges)
            line_processed = line_processed[1:-1]
            for j in line_processed:
                print(j)
                indx = j.index(delimeter_weight)
                head_vertex = int(j[:indx])
                weight = int(j[indx+1:])
                will_be_added = head_vertex, weight
                self.adj_list[node_counter].append(will_be_added)
            node_counter += 1
        file.close()
    def shortest_paths(self):
        """
        self.A becomes the shortest path list of given G from starting node.
        """
        cnt = 0
        while len(self.X) != self.n :
            edges = []
            min_len = 1000000
            min_h = ""
            for i in self.X:
                for j in self.adj_list[i]:
                    if j[0] not in self.X:
                        edges.append((i, j[0], j[1]))
            for t,h,w in edges:
                if t in self.A and self.A[t] + w < min_len:
                    min_len = self.A[t] + w
                    min_h = h
            self.X = self.X | {min_h}
            self.A[min_h] = min_len
solver = Solver(8,1)
solver.load_file("test1.txt", " ", ",")
solver.shortest_paths()
