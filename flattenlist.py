def flatten(lst):
    flist=[]
    for item in lst:
        if isinstance(item,list):
            flist.extend(flatten(item))
        else:
            flist.append(item)
    return flist
lst=[1, 2, 3, [1, 2, 3, [3, 4], 2]]
r=flatten(lst)
print(r)
