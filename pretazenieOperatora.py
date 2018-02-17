from math import hypot
from  triedy import *


bod = Bod(1, 1)
bod2 = Bod(2, 2)
bod3 = Bod(5, 0)
troj = Trojuholnik(bod, bod2, bod3)

print(troj.exists())

#print("{} + {} = {}".format(bod, cislo, bod4))
print(troj.Obvod)
print(troj.Obsah)