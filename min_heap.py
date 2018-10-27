class MinHeap:
  def __init__(self):
    self.heap_list = [None]
    self.count = 0

  def parent_idx(self, idx):
    return idx // 2

  def left_child_idx(self, idx):
    return idx * 2

  def right_child_idx(self, idx):
    return idx * 2 + 1

  def child_present(self, idx):
    return self.left_child_idx(idx) <= self.count
  
  def retrieve_min(self):
    # Empty check
    if self.count == 0:
      print("No items in heap")
      return None
    
    # Store minimum in min variable
    min = self.heap_list[1]
    
    #Swap min with last element
    self.heap_list[1] = self.heap_list[self.count]
    self.count -= 1
    self.heap_list.pop()
    self.heapify_down()
    return min

  def add(self, element):
    self.count += 1
    self.heap_list.append(element)
    self.heapify_up()

  def get_smaller_child_idx(self, idx):
    # check if we have a right child for this idx
    if self.right_child_idx(idx) > self.count:
      # we dont
      return self.left_child_idx(idx)
    else:
      #we do
      left_child = self.heap_list[self.left_child_idx(idx)]
      right_child = self.heap_list[self.right_child_idx(idx)]
      # check if right child is greater
      if left_child < right_child:
        # it isnt
        return self.left_child_idx(idx)
      else:
        #it is
        return self.right_child_idx(idx)
    
  def heapify_up(self):
    # set idx to the LAST value
    idx = self.count
    swap_count = 0
	# while there's a parent element available:
    while self.parent_idx(idx) > 0:
      # if  parent value is greater than child value at idx:
      if self.heap_list[self.parent_idx(idx)] > self.heap_list[idx]:
        # swap parent and child value
        swap_count += 1
        tmp = self.heap_list[self.parent_idx(idx)]
        self.heap_list[self.parent_idx(idx)] = self.heap_list[idx]
        self.heap_list[idx] = tmp
      # reset idx to the new parent and continue heapifying
      idx = self.parent_idx(idx)
    element_count = len(self.heap_list)
    if element_count > 10000:
      print("Heap of {0} elements restored with {1} swaps"
            .format(element_count, swap_count))
      print("")    
      
  def heapify_down(self):
    # starting with our first element
    idx = 1
    swap_count = 1
    # while there's at least one child present
    while self.child_present(idx):
      print("Heapifying down!")
      # get the smallest child's index
      smaller_child_idx = self.get_smaller_child_idx(idx)
      child = self.heap_list[smaller_child_idx]
      parent = self.heap_list[idx]  # parent is first element 
      if parent > child:
        # swap elements
        swap_count += 1
        self.heap_list[idx] = child
        self.heap_list[smaller_child_idx] = parent
      idx = smaller_child_idx
      
    element_count = len(self.heap_list)
    if element_count >= 10000:
      print("Heap of {0} elements restored with {1} swaps".format(element_count, swap_count))
      print("")  
