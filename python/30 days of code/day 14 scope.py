class Difference:
  def __init__(self, a):
    self.__elements = a
    self.maximumDifference = 0
  
  def computeDifference(self):
    for i, e1 in enumerate(self.__elements[:-1]):
      for e2 in self.__elements[i+1:]:
        diff = abs(e1 - e2)
        self.maximumDifference = max(self.maximumDifference, diff)
        
        
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
        
        
   

