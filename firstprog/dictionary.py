# Dictionary
# dictionary having it's value mutable whereas key is not..
d={"name":['a','b'] , "roll":12345 , "loc":"kanpur"}

for k in d.keys():
    print(k)

for k in d:
    print(k,d[k])

for k,v in d.items():
    print(k,v)