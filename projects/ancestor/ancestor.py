class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id in self.vertices:
            print("WARNING: That vertex already exists")
        else:
            self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")
        
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

def bfs(graph, starting_vertex):
    earliest_an = None
    #  create queue
    q = Queue()
    #  adding the starting_vertex the queue
    initital_path = [starting_vertex]
    # calling it q.enqueue
    q.enqueue(initital_path)
    #  To store visited nodes
    visited = set()
    # When the queue is not empty
    while q.size() > 0:
        # dequeue, the first vertex
         path = q.dequeue()
        #  lenght path
         path_length = len(path)
        # grabbing the last number from the path
         last_vert = path[-1]
         
         if last_vert not in visited:
             visited.add(last_vert)
             # loop over each neighbor in the graphs vertices at index of vert
             for v in graph.vertices[last_vert]:
                # make a copy of the path
                path_copy = path[:]
                # append vertex to the coppied path
                path_copy.append(v)
                # then enqueue the copied path
                q.enqueue(path_copy)

                if len(path_copy) > path_length:
                    earliest_an = path_copy
    if earliest_an:
        return earliest_an[-1]
    return -1

def earliest_ancestor(ancestors, starting_node):
    # instantiate a new graph object
    graph = Graph()
    # loop over all pairs in ancestors
    for pair in ancestors:
        # add pair[0] and pair[1] to the graph
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # Create child to parent relationship 
        graph.add_edge(pair[1], pair[0])

    return bfs(graph, starting_node)      