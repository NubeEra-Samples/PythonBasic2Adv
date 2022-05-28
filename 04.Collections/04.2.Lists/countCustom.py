def myCount(data,f):
    counter=0
    for d in data:
        if d==f:
            counter=counter+1
    return counter


x=[11,22,33,11,44,55,66,11,77,88,55,99,100,110,120]


r=myCount(x,25)

print(r)