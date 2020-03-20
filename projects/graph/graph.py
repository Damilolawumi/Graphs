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
            v = q.dequeue() # remove the first vertex out of the queue
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
        # loop over every child vertex in vertices set at the starting vertex
        for child_vertex in self.vertices[starting_vertex]:
            # if child vertex is not in visited
            if child_vertex not in visited:
                # do a recursive call to dft_recursive and pass in child vertex and the visited set as arguments
                self.dft_recursive(child_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # TODO
        q = Queue() # create a queue
        # Add a path to the starting vertex_id to the queue
        q.enqueue([starting_vertex])
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            v_path = q.dequeue() # Dequeue, the first path
            # set a vert to the last item in the path
            v = v_path[-1] 
            
            if v not in visited:
            # if vert is equal to target value
             if v == destination_vertex:
                 return v_path
             visited.add(v) # add vert to visited set
             # loop over next vert in vertices at the index of vert   
             for neighbor in self.get_neighbors(v):
                 # set a new path equal to a new list of the path
                path_copy = v_path.copy()
                # append next vert to new path
                path_copy.append(neighbor)
                # enqueue the new path
                q.enqueue(path_copy)
        return None        


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # TODO
        s = Stack() # create a stack
        s.push([starting_vertex]) # push a list holding the starting vertex id
        # Create an empty set to store visited nodes
        visited = set()
        # while the stack is not empty
        while s.size() > 0:
            # pop, the first path
            v_path = s.pop()
            # set a vert to the last item in the path
            v = v_path[-1]
           
            if v not in visited:
            # if vert is equal to destination vertex
             if v == destination_vertex:
                 return v_path #return path
            # add vert to visited set
             visited.add(v)
             # loop over next vert in vertices at the index of vert
             for neighbor in self.get_neighbors(v):
                # set a new path equal to a new list of the path (copy)
                path_copy = v_path.copy()
                # append next vert to new path
                path_copy.append(neighbor)
                 # push the new path
                s.push(path_copy)
              

    def dfs_recursive(self, starting_vertex, target_vertex, visited = None, path=None): #set default value to none
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # TODO
        if visited is  None:  # if visited is none, set visited to new set
            visited = set()
        if path is None:
            path = []
        visited.add(starting_vertex) # add starting vertex to visited set
        path = path + [starting_vertex]
        if starting_vertex == target_vertex:
            return path

        for child_vertex in self.vertices[starting_vertex]:
            if child_vertex not in visited:
                new_path = self.dfs_recursive(child_vertex, target_vertex, visited, path)
                if new_path:
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
