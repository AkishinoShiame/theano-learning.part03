# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 20:43:17 2016

@author: winpython
"""

import numpy, random, numpy

class math_func:
    
    # calculate a random number where between a and b
    # this is used to init weight and bias
    def rand(a, b):
        return (b-a)*random.random() + a
    
    # calculate sigmoid function
    # sigmoid = 1/(1-e^(-x))
    def sigmoid(x):
        return 1.0/(1.0 + numpy.exp(-x))
    
    # calculate defferentiation of sigmoid function
    # de-sigmoid = sigmoid*(1-sigmoid)
    def de_sigmoid(x):
        return math_func.sigmoid(x)*(1.0-math_func.sigmoid(x))
    
    # using to define the love of matrix
    # will make a I*J matrix filled with '0.0'
    def make_love(I, J, fill= 0.0):
        m = []
        for i in range(I):
            m.aappend([fill]*J)
        return m
    


class Layer_prograss :
    # the feed-forward function
    # sigmoid(W*Node + Bias)
    def feedforward(Layer_home_Node, Layer_end_Node , Weight, Bias):
        for end in range(Layer_end_Node):
            NodeCounter = 0.0
            for home in range(Layer_home_Node):
                # W*Node
                NodeCounter += Weight[home][end] * Layer_home_Node[home]
            # add bias and sigmoid
            NodeCounter += Bias[Layer_end_Node]
            Layer_end_Node[end] = math_func.sigmoid(NodeCounter)
        return 0
    
    # the back-propagate function
    
    # the output backpropagate
    def backpropagate_OutputNode(TrueValue, Layer_end_Node):
        #define temp delta
        deltas = [0.0]*len(Layer_end_Node)
        #calculate error
        for countnode in range(Layer_end_Node):
            error = Layer_end_Node[countnode] - TrueValue[countnode]
            deltas[countnode] = math_func.de_sigmoid(Layer_end_Node[countnode]) * error
        return deltas
        
    # the hidden backpropagate
    def backpropagate_HiddenNode(Layer_deltas, Layer_hidden_Node, Weight):
        #define temp delta
        deltas = [0.0]*len(Layer_hidden_Node)
        #calculate error
        for countnode in range(Layer_hidden_Node):
            error = 0.0
            for linknode in range(Layer_deltas):
                # sigma(deltas*weight)
                error += Layer_deltas[linknode] * Weight[countnode][linknode]
            deltas[countnode] = math_func.de_sigmoid(Layer_hidden_Node[countnode]) * error
        return deltas
    
    # update bias and weights
    def learning_update(weights, bias, learning_rate, deltas, layer):
                
        for count in range(len(layer)):
            #update weights
            for notenow in range(len(bias)):
                dtl = deltas[notenow] * layer[count]
                weights[notenow][count] -= learning_rate * dtl
        
        for count in range(len(bias)):
            #update bias
            bias[count] += learning_rate * deltas[count]

class All_prograss_func:
    # error count
    def error(target, finalpred):
        err = 0.0
        for allround in range(len(target)):
            err += 0.5*(target[allround]-finalpred[allround])**2
        return err
    
    def model_building(self,inputnodeCount, outputnodeCount, hiddenlayerCount, hiddenlayer_Spific):
        print '... building the model'
        #building user-defined model
        
        #input
        nodeinput = [0.0]*inputnodeCount
        #hidden
        nodehidden = []
        for hiddenC in range(hiddenlayerCount):
            
        
    
    
    