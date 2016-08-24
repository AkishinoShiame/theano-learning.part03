# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 00:44:05 2015

@author: winpython
"""

import os
import sys, getopt
import time
import numpy as np
from cnn_training_computation import fit
import pickle, cPickle, gzip



def run():
    print '... loading data'

    # Load the dataset
    f = gzip.open("training_data_200v6_1.pkl.gz", 'rb')
    train = cPickle.load(f)
    f.close()
    
    train_set, train_label = train
    
    data = train_set
    labels = train_label
    
    
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
    """
    """    
    # normalization
    amean = np.mean(data)
    data = data - amean
    astd = np.std(data)
    data = data / astd
    # normalise using coefficients from training data
    test_data = (test_data - amean) / astd
    valid_data = (valid_data - amean) / astd
    """
    test_data = train_set
    valid_data = train_set
    fit(data, labels)
    
    print "finished training"
   
   


if __name__ == '__main__':
    run()