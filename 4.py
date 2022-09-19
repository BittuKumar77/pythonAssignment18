# 4. Write a python program to change the value of a specific item by referring to its key
# name.

d1={100:"C",101:"C++",102:"Python",104:"Java"}
del(d1[102])
print(d1)
d1[102]='SQL'
print(d1)