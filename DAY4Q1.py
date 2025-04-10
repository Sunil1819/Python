class Poly:
    def __init__(self,*coefficient):
        self.coefficient = list(coefficient[::-1])
    def __add__(self,other):
        maxlength=max(len(self.coefficient), len(other.coefficient))
        pself=self.coefficient+[0]*(maxlength-len(self.coefficient))
        pother=other.coefficient+[0]*(maxlength-len(other.coefficient))
        r=[pself[i]+pother[i] for i in range(maxlength)]
        return Poly(*r[::-1])
    def __repr__(self):
        return f"Poly({','.join(map(str, self.coefficient[::-1]))})"
a = Poly(1, 2, 3)
b = Poly(1, 0, 1, 1, 2, 3)
c = a + b
print(c)

