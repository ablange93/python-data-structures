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
    
  # Setter | Assigns key-value pair to array. #
  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    self.array[array_index] = value

  # Getter | Retrieves key-value pair from array based on key. #
  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    # Check if there's a key at this array index
    current_array_value = self.array[array_index]
    	
    #If there's no key, then overwrite
    if current_array_value is None:
      self.array[array_index] = [key, value]
        
    #If keys are the same, then overwrite
    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
         
    #If there's a different key, then return
    #Later we'll need to have a LL to store the 2nd key
    return