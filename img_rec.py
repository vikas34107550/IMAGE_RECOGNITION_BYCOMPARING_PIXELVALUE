# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 13:40:22 2017

@author: Vikas_Singh
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce
from collections import Counter
i=Image.open('Images/numbers/y0.5.png')
iar=np.asarray(i)
#print (iar)
#plt.imshow(iar)
plt.show()
'''def thresold(imagearray):
    balancear=[]
    newar=imagearray
    for eachrow in imagearray:
        for eachpix in eachrow:
            avgnum=reduce(lambda x, y: x + y, eachpix[:3])/(len(eachpix[:3])) 
            balancear.append(avgnum)
            #print (len(balancear))
    balance=reduce(lambda x, y: x + y, balancear)/(len(balancear))  
    #print ("balance is :" + str(balance))
    for eachrow in newar:
        for eachpix in eachrow:
            if (reduce(lambda x, y: x + y, eachpix[:3])/(len(eachpix[:3]))>balance):
                eachpix[0]=255
                eachpix[1]=255
                eachpix[2]=255
                eachpix[3]=255
            else:
                eachpix[0]=0
                eachpix[1]=0
                eachpix[2]=0
                eachpix[3]=255
    

    


i1=Image.open('Images/numbers/0.1.png')
iar1=np.array(i1)
i2=Image.open('Images/numbers/y0.4.png')
iar2=np.array(i2)
i3=Image.open('Images/numbers/y0.5.png')
iar3=np.array(i3)

thresold(iar1)
thresold(iar2)
thresold(iar3)



ax1=plt.subplot2grid((8,6),(0,0),rowspan=4,colspan=3)
ax2=plt.subplot2grid((8,6),(4,0),rowspan=4,colspan=3)
ax3=plt.subplot2grid((8,6),(0,3),rowspan=4,colspan=3)

ax1.imshow(iar1)
ax2.imshow(iar2)
ax3.imshow(iar3)
'''

def createExamples():
    numberArrayExample=open('numArEx.txt','a')
    numberWeHave=range(0,10)
    versionWeHave=range(1,10)
    for eachNum in numberWeHave:
        for eachVer in versionWeHave:
            imgFilePath=('images/numbers/' + str(eachNum)+ '.' + str(eachVer) + '.png')
            ei=Image.open(imgFilePath)
            eiar=np.array(ei)
            eiar1=str(eiar.tolist())
            lineToWrite=str(eachNum)+ '::'+ eiar1 + '/n'
            (lineToWrite)
            numberArrayExample.write(lineToWrite)
#createExamples()





def whatNumIsThis(filePath):
    matchedAr=[]
    loadExamps=open('numArEx.txt','r').read()
    loadExamps=loadExamps.split('/n')
    i=Image.open(filePath)
    iar=np.array(i)
    iar1=iar.tolist()
    
    inQuestion=str(iar1)
    
    for eachExample in loadExamps:
        if (len(eachExample) > 3):
            splitEx=eachExample.split('::')
            currentNum=splitEx[0]
            currentAr=splitEx[1]
            eachPixEx=currentAr.split('],')
            eachPixInq=inQuestion.split('],')
            x=0
            while (x < len(eachPixEx)):
                if(eachPixEx[x]==eachPixInq[x]):
                    matchedAr.append(int(currentNum))
                x=x+1
            
    X=Counter(matchedAr)
    print (X)
    print (len(matchedAr))
     

whatNumIsThis('images/test5.png')
















