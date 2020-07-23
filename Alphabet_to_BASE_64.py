alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
y= 0; BASE= 11111111
while True:
    o= ''; m= input("Sentence: ")
    for i in m:
        a= ord(i); b= a; z= 0
        while a>1:
            n= 0; b= a
            while not a == 1:a= a//2; n+= 1
            z+= 1 * 10 ** n
            a= b-(2 ** n); n= 0
        if a == 1:z += 1
        c = BASE-(BASE - z)
        if len(str(c))<8:
            d = (8-len(str(c)))*'0'
        x= str(d)+ str(c); o+= x; y+= 1
    e=len(o); r= 0; t= ''; u= []; l= []
    if e%6 == 0:
        for i in o:
            r+= 1; t+= i
            if r == 6:u.append(t); t= ''; r= 0
    elif e%6 == 2:
        o += '0000'
        for i in o:
            r+= 1; t+= i
            if r == 6:u.append(t); t= ''; r= 0
    elif e%6 == 4:
        o += '00'
        for i in o:
            r+= 1; t+= i
            if r == 6:u.append(t); t= ''; r= 0
    for f in u:
        k= 0; h= 5
        for g in f:k+= int(g)* 2**h; h-= 1
        l.append(k)
    for p in range(len(l)):q= l[p]; print(alphabet[q],end='')
    if e%6 == 2:print("==")
    elif e%6 == 4:print("=")
    print('\n')
