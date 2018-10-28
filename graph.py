# import Vertex class #
from vertex import Vertex

class Graph:
  def __init__(self, directed=False):
    self.directed = directed
    self.graph_dict = {}
    
  def add_vertex(self, vertex):
    print("Adding " + vertex.value)
    self.graph_dict[vertex.value] = vertex

  def add_edge(self, from_vertex, to_vertex, weight=0):
    print("Adding edge from " + from_vertex.value + " to " + to_vertex.value)
    # Directed graph
    self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
    #If graph is Undirected
    if self.directed == False:
      self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)
      
  def find_path(self, start_vertex, end_vertex):
  	print("Searching from " + start_vertex + " to " + end_vertex)
    start = [start_vertex]
    while len(start) > 0:
      current_vertex = start.pop(0)
      print("Visiting " + current_vertex)
      # if current matches end, then path is found
      if current_vertex == end_vertex:
        return True
      # Keep looking until match
      vertex = self.graph_dict[current_vertex]
      next_vertices = vertex.get_edges()
      start += next_vertices
    return False
      
   