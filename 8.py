# 8. Write a python program to convert two lists into a dictionary in a way that item from
# list1 is the key and item from list2 is the value.

l1=[10,20,30,40,50]
l2=['C','C++','Java','Python','React']
print("key:",l1)
print("values:",l2)
d1={l1[i]:l2[i] for i in range(len(l1))}
print("Dict is : "+str(d1))