
from abc import ABC,abstractmethod
class polygon(ABC):
    @abstractmethod
    def sides(self):
        pass
class traingle(polygon):
    def sides(self):
        print("traingle has 3 sides")
class pentagon(polygon):
    def sides(self):
        print("pentagon has 5 sides")
class hexagon(polygon):
    def sides(self):
        print("hexagon has 6 sides")

t=traingle()
t.sides()

p=pentagon()
p.sides()

h=hexagon()
h.sides()

# traingle has 3 sides
# pentagon has 5 sides
# hexagon has 6 sides
