# HASH MAP #
class HashMap:
  # ARRAY | Create the array
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]
    
  # HASH FUNCTION | User inputs a key which is converted into bytes
  def hash(self, key, count_collisions=0):
    hash_code = sum(key.encode())
    # Hash function now passes CollisionsCounter as part of open addressing system 
    return hash_code + count_collisions

  # COMPRESSOR | Ensure hash code will fit inside the array
  def compressor(self, hash_code):
    return hash_code % self.array_size
    
  # SETTER | Assigns key-value pair to array index
  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]
    
    # If array value is empty, then assign key-value
    if current_array_value is None:
      self.array[array_index] = [key, value]
      return
    
    # If keys match, then overwrite value
    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return
    
    # COLLISION EVENT | Key exists and is different from input key.
    # Use open addressing to assign the value 
    number_collisions = 1

    while current_array_value[0] != key:
      new_hash_code = self.hash(key, number_collisions)
      new_array_index = self.compressor(new_hash_code)
      current_array_value = self.array[new_array_index]
      
      # If new array value is empty, then assign key-value
      if current_array_value is None:
        self.array[new_array_index] = [key, value]
        return
      
      # If new keys match, then overwrite value
      if current_array_value[0] == key:
        self.array[new_array_index] = [key, value]
        return
      
      # SUB-COLLISION EVENT | Increment counter and re-iterate
      number_collisions += 1
      
  # GETTER | Retrieves key-value pair from array based on key. #
  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]
    
    # If array value is empty, return None
    if possible_return_value is None:
      return None
      
    # If keys match, return value
    if possible_return_value[0] == key:
      return possible_return_value[1]
    
    # COLLISION EVENT | Key exists and is different from input key.
    # Use open addressing to retrieve the value 
    retrieval_collisions = 1

    while (possible_return_value != key):
      new_hash_code = self.hash(key, retrieval_collisions)
      retrieving_array_index = self.compressor(new_hash_code)
      possible_return_value = self.array[retrieving_array_index]

      # If array value is empty, return None
      if possible_return_value is None:
        return None
	  
	  # If keys match, return value
      if possible_return_value[0] == key:
        return possible_return_value[1]
	  
	  # SUB-COLLISION EVENT | Increment counter and re-iterate
      number_collisions += 1
    return
    
# MAIN #
hash_map = HashMap(15)

hash_map.assign('gabbro', 'igneous')
hash_map.assign('sandstone', 'sedimentary')
hash_map.assign('gneiss', 'metamorphic')

print(hash_map.retrieve('gabbro'))
print(hash_map.retrieve('sandstone'))
print(hash_map.retrieve('gneiss'))
      