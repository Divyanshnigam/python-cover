# ___________LIST_______________

l=[]
l.append(10)
l.append(20)
l.append(30)
l.append(10)
l.append('abc')
l[0]=56
print(l)

# oder is imp
#duplicate
#growable
#values enclsed with []
#mutable







mylist = ["div" , "joe","alex","noob","brat","bot"]
print(mylist)
mylist.sort()
print(mylist)




# ______TUPLE _____________
print("#############  TUPLE  ##########")
#immutable

t=(10,20,30,'tuple')
#b=t[0]  not done as its immutalbe
print(t[1:3])
#t[0]=100











mytupple = (1,2,2,4,3,10,8,7)
print(mytupple)
tup_to_list= list(mytupple)
tup_to_list.sort()
print(tup_to_list)

tupleofstr=("abc","def","ghi","jkl")
print(tupleofstr)

print("######################  DICTIONARY   #################################")
# stores key and a value to that key


dict1= {"divyansh":"nigam", "vishwash":"bajpai","elon":"musk","peter":"england"}
print(dict1)

#

# dict2= dict1 >>>> but this will make a change in the original dictionary dict1 when modify dict2 so instead use a copy function
dict2= dict1.copy()
dict2.pop("vishwash","bajpai")
print(dict2)

dict1.update({"albert":"einsten"})
print(dict1)

"""
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

"""