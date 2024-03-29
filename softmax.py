import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    expL = np.exp(L)
    sumExpL = sum(expL)
    OP = []
    
    for num in expL:
       OP.append(num/sumExpL)
    return OP
