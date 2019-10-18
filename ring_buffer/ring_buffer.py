class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current == 5:
      self.current = 0
    self.storage[self.current] = item
    self.current += 1


  def get(self):
    return [el for el in self.storage if el]