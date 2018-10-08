# HASH MAP #
class HashMap:
  # Array | Create the array
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]
    
  # Hash | User inputs a key which is converted into bytes
  def hash(self, key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code

