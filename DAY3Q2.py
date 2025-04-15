def transform(data):
    output=[]
    for outer in data:
        ioutput=[]
        for middle in outer:
            ilist=[list(map(int, elem.strip('()').split(','))) for elem in middle]
            ioutput.append(ilist)
        output.append(ioutput)
    return output
input_s=[[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
result=transform(input_s)
print(result)