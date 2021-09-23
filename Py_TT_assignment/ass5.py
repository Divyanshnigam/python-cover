x="aabbbcccc"
the_count=1;
for i in range(0,len(x)-2):
    if x[i]==x[i+1]:
        the_count=the_count+1
    else:
        print(str(the_count) + x[i],end='')
        the_count=1

print(str(the_count+1) + x[i],end='')
