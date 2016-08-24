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

# read filename tag
my_data = np.genfromtxt('data.csv', delimiter = ',')

final_output = np.zeros((200,147456),dtype=np.float32)
final_label = np.zeros((200,),dtype=np.int64)

def pack():
    
    print "Labling work ..."
    test = 0
    for i in range(2):
        for j in range(100):
            final_label[test]=j
            test += 1
    print "finished labeled ..."
    
    filename_use = 0
    count = 0
    
    for i in range(100):
        for j in range(100):
            print "reading", int(my_data[j][i]), "..."
            pil_im = Image.open("data_pic/" + str(int(my_data[j][i])) + ".jpg").convert('L')
            pil_im = pil_im.resize((512, 288), Image.BILINEAR )
            pil_im = np.array(pil_im)
            fig = plt.figure()
            plotwindow = fig.add_subplot()
            plt.imshow(pil_im, cmap='gray')
            
            note = 0
            for L in range(288):
                for K in range(512):
                    final_output[count][note] = ((255 - pil_im[L][K])/225.)
                    note += 1
            count += 1
            if(count%200 == 0):
                count = 0
                filename_use += 1
                print "Starting cpickle"
                outputandlabel = final_output, final_label
                f = gzip.open("training_data_200v7_" + str(filename_use) + ".pkl.gz", 'wb')
                cPickle.dump(outputandlabel, f)
                f.close()
                print "Finished cPickle..."

    print "\ ! congradulation ! /" 
    print " finished"

if __name__ == '__main__':
    pack()