import numpy as np
from dataclasses import dataclass


x = np.fromfunction(lambda i,j: i**2 + j**2, (10,10))
for t in range(1,10):
    x = np.fromfunction(lambda i,j: (i-t)**2 + (j-t)**2, (10,10))
    print("step")

x = ["a", "b", "c"]

x = {"a": 4, "b": 5, "c": 6}


@dataclass
class Point:
    x: int
    y: int
    z: int

x = Point(1,2,3)

print("end")
