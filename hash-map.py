# HASH MAP #
class HashMap:
  # Array | Create the array
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]
    
  # Hash | User inputs a key which is converted into bytes. #
  def hash(self, key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code

  # Compressor | Ensure hash code will fit inside the array. #
  def compressor(self, hash_code):
    return hash_code % self.array_size
    
  # Setter | Assigns key-value pair to array index. #
  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]
    
    # Check if key-value pair exists at array index. #
    if current_array_value is None:
      self.array[array_index] = [key, value]
      return
    
    # Check if key input matches existing key. #
    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return
    
    # Existing key is different, will add LinkedList to hold different keys #
    # at this array index.   												#
    return  
    

  # Getter | Retrieves key-value pair from array based on key. #
  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    return self.array[array_index]