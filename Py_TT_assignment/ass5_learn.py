from itertools import groupby
str="AABCCABBPPB"
for k,g in groupby(str):
    print("%d%s"%(len(list(g)),k),end="")