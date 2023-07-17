from string import *
from itertools import product
value = ascii_letters + digits +punctuation
l=[]
for i in range(1,3):
    for j in product(value,repeat=i):
        word=" ".join(j)
        l.append(word)
print(l)