import sys
import os

class area:
        def __init__(self):
                pass
        def rectangle(l,b):
                print(l * b)
        def triangle(b,h):
                print((1/2) * b * h)
        @staticmethod
        def print():
                print("Calculating the area of polygons")

area.print()
ar = area
ar.rectangle(3,4)
ar.triangle(4,6)
