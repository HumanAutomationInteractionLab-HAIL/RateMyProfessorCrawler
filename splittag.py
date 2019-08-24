import re
import pandas as pd

def splittag(Tag):
    templist=re.split('\([0-9]+\)',Tag)
    templist= list(filter(None, templist))
    tempnumber=re.findall('\([0-9]+\)',Tag)
    tempnumber= list(filter(None, tempnumber))

    for index,value in enumerate(templist):
        templist[index]=value.strip()
    

    for index,value in enumerate(tempnumber):
        tempnumber[index]=value.strip(')').strip('(')
        

    return templist,tempnumber

