# try:
#     a = int(input("input number"))
#     b = int(input("input number"))
#     c=a/b
#     print("Result is ",c)
# except Exception as e:
#     print(e)

try:
    a = int(input("input number"))
    b = int(input("input number"))
    c=a/b
    print("Result is ",c)
    list1=[2,3]
    i=int(input("enter index"))
    print(list1[i])
except Exception as e:
    print(e)
finally:
    print("finally")
#
# else:  # else executed when theres no exception
#     print("else")