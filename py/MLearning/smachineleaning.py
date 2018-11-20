from numpy import dot, random, array
from time import time


class neuralnet:
    def __init__(self, *args, **kwargs):
        random.seed(round(time()))
        self.weight = random.random((2, 1))

    def train(self, inputs, outputs, rep):
        for repetition in range(rep):
            output = self.think(inputs)
            error = outputs.T-output
            adjustment = .01*dot(inputs.T, error)
            self.weight += adjustment

    def think(self, inputs):
        return dot(inputs, self.weight)


neu = neuralnet()
neu_inputs = array([[2,1],[3,1],[6,2],[10,2]])
nue_outputs = array([[2,3,12,20]])
neu.train(neu_inputs,nue_outputs,10000)
print(neu.weight)
print(neu.think(array([8,2])))