d= {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
list1=['god','jul']
x=d.keys()
print(x)
list2=[]
d2={}
#reversing a dictionary
for k,v in d.items():
    d2[v]=k

def translate(d,list1):
    for word in list1:
        for k in d.keys():
            if word == k:
                list2.append(d[k])
    return list2

print(translate(d2,list1))
