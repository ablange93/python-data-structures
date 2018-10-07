from node import Node

# LINKED LIST #
class LinkedList():
  def __init__(self, value=None):
    self.head_node = Node(value)
    
  def get_head_node(self):
    return self.head_node
    
  def insert_beginning(self, new_value):
    #instantiate new node
    new_node = Node(new_value)
    #use set_next_node link it to the current head
    new_node.set_next_node(self.head_node)
    #set head_node to this new node that is now the head
    self.head_node = new_node   

  def stringify_list(self):
    resultString = ""
    current_node = self.head_node
    while current_node:
      if current_node.value != None:
        resultString += str(current_node.value) + "\n"
      current_node = current_node.get_next_node()
    return resultString
      
  def remove_node(self, value_to_remove):
    current_node = self.head_node
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.next_node = next_node.get_next_node()
          current_node = None
        else:
          current_node = next_node

  def remove_node(self, value_to_remove):
    current_node = self.head_node
    #compare using get_value and NOT .value because here were comparing the node's value to the value_to_remove argument, and not a string where wed need to concancentate multiple values
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        current_next_node = current_node.get_next_node()
        if current_next_node.get_value() == value_to_remove:
          current_node.next_node = current_next_node.get_next_node()
          current_node = None
        else:
          current_node = current_next_node
          