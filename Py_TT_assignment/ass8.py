#list=[{"Name":"Amit","Age":"20"},{"Name":"anil","Age":"26"},{"Name":"sunil","Age":"25"},]
l=[]
while True:
    d={}
    key=input("enter name:")
    value=int(input("enter age:"))
    d[key] = value
    l.append(d)
    x=input("Want to enter more y\n:")
    if x=='n':
        break

m=-1
for k,v in d.items():
    if d[key] > m:
        m=d[key]
print("max age is: ", m , d.key())
print(l)
