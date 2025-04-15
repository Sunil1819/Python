import os
def findlargestfile(directory):
    msize=0
    mfile=None
    for dpath,dnames,fnames in os.walk(directory):
        for fname in fnames:
            filepath=os.path.join(dpath,fname)
            if os.path.isfile(filepath):
                fsize=os.path.getsize(filepath)
                if fsize>msize:
                    msize=fsize
                    mfile=filepath
    return mfile,msize
directory=r'C:\Users\Sunil\handson'
lfile,size=findlargestfile(directory)
if lfile:
    print(f"Largest file: {lfile}")
    print(f"Size:{size} bytes")
else:
    print("No files found.")

