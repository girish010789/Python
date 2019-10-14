from abc import ABC, abstractmethod
class house(ABC):
##add a decorator
        @abstractmethod
        def living_room(self):
                pass
        @abstractmethod
        def bedroom(self):
                pass
        @abstractmethod
        def kitchen(self):
                pass
class area(house):
        def __init__(self,ll,lw):
                self.__ll = ll
                self.__lw = lw
        def living_room(self):
                print(self.__ll * self.__lw)
        def bedroom(self,bl,bw):
                print(bl * bw)
        def kitchen(self,ka,kb,kh):
                print(((ka + kb)/2) * kh)

ar = area(10,12)
ar.living_room()
ar.bedroom(10,12)
ar.kitchen(7,9,12)
