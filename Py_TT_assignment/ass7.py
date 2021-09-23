from collections import Counter
specilaties={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
def counter(x):
    if x == 'O':
        print("Orthopedics")
    elif x == 'E':
        print("ENT")
    else:
        print("Pediatrics")

provider=[101,"P",102,"O",103,"O",104,"E"]
my_list=[]
for i in provider:
    if type(i) == str:
        my_list.append(i)

m=-1
for k,v in Counter(my_list).items():
    if v>m:
        m=v
print(m)
for k in Counter(my_list).keys():
    if Counter(my_list) [k]==m:
        counter(k)
