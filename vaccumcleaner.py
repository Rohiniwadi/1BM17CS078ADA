

d={'A':0,'B':0}
d['A'] = int(input())
d['B'] = int(input())
print(d)
vloc = int(input())
while (d['A']!=0 or d['B']!=0):
    if vloc==0:
        if d['A']==1:
            print("location A is dirty")
            d['A']=0
            print('location A cleaned')
            print('moving to location B')
            if d['B']==1:
                d['B']=0
                print('location B cleaned')
        else:
            print('moving to location B')
            if d['B']==1:
                d['B']=0
                print('location B cleaned')

    else:
        if d['B']==1:
            print("location B is dirty")
            d['B']=0
            print('location B cleaned')
            print('moving to location A')
            if d['A']==1:
                d['A']=0
                print('location A cleaned')
        else:
            print('moving to location A')
            if d['A']==1:
                d['A']=0
                print('location A cleaned')
    
