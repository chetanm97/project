import switch as s
import craller as c

predicted=[]
a,b=s.pre_class()
for text1 in a:
    y=c.classify(text1)
    predicted.append(y)
    print(predicted)
