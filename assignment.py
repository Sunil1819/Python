D1={'ok': 1, 'nok': 2}
D2={'ok': 2, 'new': 3}
D1unionD2={**D1,**D2}
D1intersectionD2={k:D1[k] for k in D1 if k in D2}
D1minusD2={k:D1[k] for k in D1 if k not in D2}
d={}
for k in set(D1)|set(D2):
    d[k]=D1.get(k,0)+D2.get(k,0)
print(D1unionD2)
print(D1intersectionD2)
print(D1minusD2)
print(d)
