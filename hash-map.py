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
    self.array[self.compressor(self.hash(key))] = value

  # Getter | Retrieves key-value pair from array based on key. #
  def retrieve(self, key):
    value = self.array[self.compressor(self.hash(key))]
    return value