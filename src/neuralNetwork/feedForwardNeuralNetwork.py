import numpy as np

from neuralNetwork.structure.layer import Layer

class NeuralNetwork(object):
    def __init__(self):
        self.layers = []

    def appendLayer(self, layer):
        assert isinstance(layer, Layer)

        self.layers.append(layer)

    def canFire(self):
        return len(self.layers) > 1

    def fire(self, input):
        assert isinstance(input, (np.ndarray, np.generic))
        assert len(input[0]) == self.layers[0].size
        assert self.canFire()

        self.layers[0].result = input

        for layer in self.layers:
            layer.propagate()

        return self.layers[len(self.layers) - 1].result

    def backPropagation(self, target):
        for layer in reversed(self.layers):
            target = layer.backPropagate(target)

        for layer in self.layers:
            layer.applyDeltaWeights()

        return self.layers[len(self.layers) - 1].error

    # Used for PSO NN training
    def getAllWeights(self):
        weights = []
        for layer in self.layers:
            weights += layer.getWeights()

        return weights

    # Used for PSO NN training
    def setAllWeights(self, weights):
        for layer in self.layers:
            weights = layer.setWeights(weights)

    # Used for PSO NN training
    def getMSE(self):
        last = self.layers[len(self.layers) - 1]
        error = last.error
        outUnits = last.size
        return np.mean(np.square(difference))

    def __str__(self):
        res = ""
        for layer in self.layers:
            res += str(layer)
        return res