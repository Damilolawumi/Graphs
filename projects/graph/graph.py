"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {} # adjacency list (dictionary) # adjacency matrix (2d list or array)

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # add vertex
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
         # add edges
        if v1 in self.vertices and v2 in self.vertices: # check that v1 and v2 exist in the vertices dictionary
            self.vertices[v1].add(v2) # add v2 to the vertices at v1
        else:
            # raise and exception and give an error
            raise IndexError("That vertex does not exist")    


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a queue
        q = Queue()
        # create a set to store our visited vertices
        visited = set()
        q.enqueue(starting_vertex) #put starting node in the queue

        while q.size() > 0: # while queue is not empty
            v = q.dequeue() # pop the first vertex out of the queue
            if v not in visited: # if that vertex has not been visited
                visited.add(v) # mark as visited 
                print(v)
                for next_vertex in self.vertices[v]: # get adjacent edges and add to list
                    q.enqueue(next_vertex) # enqueue the next vertex
        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack() # create a stack
        visited = set() # create a set to store our visited vertices
        s.push(starting_vertex) #put starting node in the queue

        while s.size() > 0: # while stack is not empty
            v = s.pop() # remove the first vertex out of the stack
            if v not in visited: #if that vertex has not been visited
                visited.add(v) #mark as visited
                print(v)
                for next_vertex in self.vertices[v]: # iterate over the child vertices of the current vertex
                    s.push(next_vertex) # push the next vertex

    def dft_recursive(self, starting_vertex, visited= None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # TODO
        # if visited is none, set visited to new set
        if visited is None:
            visited = set()
        # add starting vertex to visited set
        visited.add(starting_vertex)
        # print starting vertex
        print(starting_vertex)
        # if vertex isn't in visited set, recurse
        for vertex in self.vertices[starting_vertex]:
            if vertex not in visited:
                self.dft_recursive(vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # TODO
        q = Queue()
        # Add A PATH TO the starting vertex_id to the queue
        q.enqueue([starting_vertex])
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue, the first PATH
            v_path = q.dequeue()
            # GRAB THE LAST VERTEX FROM THE PATH
            v = v_path[-1]
            # CHECK IF IT'S THE TARGET
                # IF SO, RETURN THE PATH
            if v not in visited:
            # Check if it's been visited
             if v is destination_vertex:
                 return v_path
            # If it has not been visited...
                # Mark it as visited
             visited.add(v)
                # Then add A PATH TO all neighbors to the back of the queue
                    # (Make a copy of the path before adding)
             for neighbor in self.get_neighbors(v):
                path_copy = v_path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # TODO
        s = Stack()
        # Add A PATH TO the starting vertex_id to the queue
        s.push([starting_vertex])
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while s.size() > 0:
            # Dequeue, the first PATH
            v_path = s.pop()
            # GRAB THE LAST VERTEX FROM THE PATH
            v = v_path[-1]
            # CHECK IF IT'S THE TARGET
                # IF SO, RETURN THE PATH
            if v not in visited:
            # Check if it's been visited
             if v is destination_vertex:
                 return v_path
            # If it has not been visited...
                # Mark it as visited
             visited.add(v)
                # Then add A PATH TO all neighbors to the back of the queue
                    # (Make a copy of the path before adding)
             for neighbor in self.get_neighbors(v):
                path_copy = v_path.copy()
                path_copy.append(neighbor)
                s.push(path_copy)

    def dfs_recursive(self, starting_vertex, target_vertex, visited = None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # TODO
        if visited is  None:
            visited = set()
        if path is None:
            path = []
        #  if it's at the target value, return the path
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)
            if starting_vertex is target_vertex:
               return path_copy 
        #  It calls for the dfs recursive on each unvisited neighbor
            for neighbor in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(neighbor, target_vertex, visited, path_copy)
                if new_path is not None:
                    return new_path

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
