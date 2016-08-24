# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 02:31:03 2015

@author: winpython
"""

import os
import sys, getopt
import time
import numpy as np
from cnn_training_computation import fit, predict
import pickle, cPickle

from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
from PIL import Image


def run():
    print '... loading data'
    
    test_set = np.zeros((200,147456),dtype=np.float32)
    pil_im = Image.open( "P_20160110_154256.jpg" ).convert('L')
    pil_im = pil_im.resize((512, 288), Image.BILINEAR )
    pil_im = np.array(pil_im)
    fig = plt.figure()
    plotwindow = fig.add_subplot()
    plt.imshow(pil_im, cmap='gray')
    plt.show()
    note = 0
    for j in range(288):
        for k in range(512):
            test_set[0][note]= ((255 - pil_im[j][k])/225.)
            note += 1
    """
    # read the data, labels
    data = np.genfromtxt("data/mnist_train.data")
    print ". .",
    test_data = np.genfromtxt("data/mnist_test.data")
    print ". .",
    valid_data = np.genfromtxt("data/mnist_valid.data")
    labels = np.genfromtxt("data/mnist_train.solution")
    """
    print ". . finished reading"
    """
    # DO argmax
    labels = np.argmax(labels, axis=1)
    print labels
    
        
    # normalization
    amean = np.mean(data)
    data = data - amean
    astd = np.std(data)
    data = data / astd
    # normalise using coefficients from training data
    test_data = (test_data - amean) / astd
    valid_data = (valid_data - amean) / astd
    """
    
    #fit(data, labels)
    print "開始預測..."
    rv = predict(test_set)



    # UNDO argmax and save results x 2
    r = rv
    N = len(r)
    res = np.zeros((N, 20))
    for i in range(N):
        res[i][r[i]] = 1
        
    tag = ['青椒牛肉燴飯','牛肉燴飯','滑蛋牛肉燴飯','滑蛋羊肉燴飯','雞腿飯'
    ,'雞排飯','排骨飯','鱈魚飯','卡拉雞腿飯','裹粉排骨飯','蠔油香菇雞'
    ,'黑胡椒牛柳','青菜豆腐湯','糖醋排骨','辣子雞丁','五更腸旺'
    ,'牛肉炒麵','肉絲炒麵','蛋花湯','燕丸湯']
    print "=================================================================="
    print " "
    print " "
    print "predict Tag  : [ 0 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 19 ]"
    print " "
    print "  ----------------------------------------------------  "
    print " "
    print "predict Value:",
    print tag[r[0]]
    print " "
    print " "
    print "=================================================================="
    
    #np.savetxt("test.predict", res, fmt='%i')
    
    print "finished predicting."
   


if __name__ == '__main__':
    run()