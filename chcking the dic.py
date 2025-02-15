hi ={"a":2,"b":2,"c":2,"d":6}
print("THe original Dic"+str(hi))
F=2
m=0
for key in hi:
    if hi[key]==F:
        m= m+1

print("The frequency of dic is",m)