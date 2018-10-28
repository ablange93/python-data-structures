class Vertex:
  def __init__(self, value):
    self.value = value
    self.edges = {}

  def add_edge(self, vertex, weight=0):
    print("Adding edge to " + vertex)
    self.edges[vertex] = weight    
    
  def get_edges(self):
    # Dictionary keys are vertices
    dict_keys = self.edges.keys()
    list_vertices = list(dict_keys)
    return list_vertices
