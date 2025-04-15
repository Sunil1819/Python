from collections import Counter
input_str="Hello world and Hello Earth"
input_str=input_str.lower()
listofwords=input_str.split()
print(listofwords)
wordcount=Counter(listofwords)
print(wordcount)
for w,c in wordcount.items():
    print(f"{w},{c}")