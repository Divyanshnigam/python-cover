d= {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
list1=['happy','christmas']
x=d.keys()
print(x)
list2=[]

def translate(d,list1):
    for word in list1:
        for k in d.keys():
            if word == k:
                list2.append(d[k])
    return list2

print(translate(d,list1))



