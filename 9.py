# 9. Write a python program to merge two python dictionaries into one dictionary.

d1={103:'hero',106:'Pulsar',109:'Honda'}
d2={101:'Splender',102:'Activa',104:'jupitar'}

dict1=d1.copy()
dict1.update(d2)
print(dict1)