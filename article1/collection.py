import switch as s
import craller as c

predicted=[]
count=0
count2=0
a,b=s.pre_class()
for text1 in a:
    y=c.classify(text1)
    predicted.append(y)
    for pred in predicted:
        if pred == 'NPOLITICS':
            count+=1
        else:
            count2+=1
    print('political data:'+str(count))
    print('not political data:'+str(count2))
    print('percentage:'+str(count/(count+count2)))
