# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 04:03:19 2015

@author: winpython
"""

from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cPickle, pickle
import gzip


final_output = np.zeros((10000,147456),dtype=np.float32)
final_label = np.zeros((10000,),dtype=np.int64)

for i in range(10000):
    print "reading", i, "..."
    pil_im = Image.open( "data_pic/" + str(i+1) + ".jpg" ).convert('L')
    #imshow(np.asarray(pil_im)) # before resize
    pil_im = pil_im.resize((512, 288), Image.BILINEAR )
    pil_im = np.array(pil_im)
    fig = plt.figure()
    plotwindow = fig.add_subplot()
    plt.imshow(pil_im, cmap='gray')
    plt.show()
    #print("test")
    #print(pil_im)
    note = 0
    for j in range(288):
        for k in range(512):
            final_output[i][note]= ((255 - pil_im[j][k])/225.)
            note += 1

print " "
print "Finished Picture..."
print "Starting label"
count = 0
for i in range (100):
    for j in range (100):
        final_label[count] = (i+1)
        count += 1
print "Finished Labeling..."

print "Starting cpickle"
#outputandlabel = final_output, final_label
f = gzip.open("training_data_200v4.pkl.gz", 'wb')
for i in range(10000):
    cPickle.dump(final_output[i], f)
cPickle.dump(final_label, f)
f.close()
print "Finished cPickle..."
print "\ ! congradulation ! /" 
       
#f = open("pic1.txt", "r")
'''
imshow(np.asarray(pil_im)) # before resize
pil_im = pil_im.resize((28, 28), Image.BILINEAR )


pil_im = np.array(pil_im)

#print(np.array(pil_im))
#imshow(np.asarray(pil_im))

fig = plt.figure()
plotwindow = fig.add_subplot()
plt.imshow(pil_im, cmap='gray')
plt.show()

print("test")
print(pil_im)

'''