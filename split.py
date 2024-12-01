def num_split(arr):
    a,p= arr,arr
    b,f = 1,0
    d = []
    while a!=0:
        if a<0:
            a = a*-1
        while a%b>=0:
            if b>a:
                b //=10
                break
            else:
                b *= 10
                f += 1
        c = ((a//b)*b)
        d.append(c)
        a -= c
    while f!=0:
        if f==len(d):
            break
        else:
            d.append(0)
        
    if p>0:
        print(d)
    elif p<0:
        for i in range(len(d)):
            d[i] = -d[i]
        print(d)
num_split(39)
num_split(-434)
num_split(100)