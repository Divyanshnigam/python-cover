d={"their":"their" , "bussiness":"bissiness" , "windows":"windmill" , "were":"wear" ,"sample":"sample","wait":"wiat"}


for k,v in d.items():
    if len(k) != len(d[k]):
        print("WRONG")
    elif k == v:
        print("CORRECT")
    elif k!=v:
        count=0

        for i in range(len(k)):
            if k[i]!=v[i]:
                count=count+1
        if count<3:
            print("ALMOST CORRECT")
        else:
            print("WRONG")

