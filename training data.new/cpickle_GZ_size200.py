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


final_output = np.zeros((200,147456),dtype=np.float32)
final_label = np.zeros((200,),dtype=np.int64)

def packet(data_name,label_name,file_name):
    for i in range(200):
        print "reading", i, "..."
        pil_im = Image.open( "data_pic/" + str(i+data_name) + ".jpg" ).convert('L')
        #imshow(np.asarray(pil_im)) # before resize
        pil_im = pil_im.resize((512, 288), Image.BILINEAR )
        pil_im = np.array(pil_im)
        fig = plt.figure()
        plotwindow = fig.add_subplot()
        plt.imshow(pil_im, cmap='gray')
        #plt.show()
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
    for i in label_name:
        for j in range (100):
            final_label[count] = j
            count += 1
    print "Finished Labeling..."
    
    print "Starting cpickle"
    outputandlabel = final_output, final_label
    f = gzip.open("training_data_200v6_" + str(file_name) + ".pkl.gz", 'wb')
    cPickle.dump(outputandlabel, f)
    f.close()
    print "Finished cPickle..."
    print "\ ! congradulation ! /" 
    print str(file_name) + "/50 finished"
    
if __name__ == '__main__':
    for dat in range(50):
        packet(200*dat+1,[2*dat+1,2*dat+2],dat+1)