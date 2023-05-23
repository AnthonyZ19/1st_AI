import numpy as np

I = [0.8, 0.54, 0.26, 0.92, 0.48]

class NeuralNetworkL:
    def __init__(self, inputs, neurons):
        self.Weights = np.random.randn(inputs, neurons)*.10
        self.Bias = np.random.randn(neurons)
    def Weights_Bias(self, inputs, neurons):
        self.Weights1 = np.random.randn(inputs, neurons)*.10
        self.Bias1 = np.random.randn(neurons)
    def Layer(self, inputs):
        LayerOutput = np.dot(inputs ,self.Weights) + self.Bias
        return Layer1Output
    def ReLU(self, inputs):
        i = 0
        while i < len(inputs):
            if inputs[i] < 0:
                inputs[i]=0
            i += 1
        return inputs
    def SoftMax(inputs):
        output = np.exp(inputs)/(np.exp(inputs).sum())
        return output
    def CrossEntropy(length, prediction, answer):
        np.sum
        

NNL1 = NeuralNetworkL(len(I), 6)
print("Weights: " + str(NNL1.Weights))
print("Bias's: " + str(NNL1.Bias))
print(NNL1.Layer(I))
print(NNL1.ReLU(NNL1.Layer(I)))
NNL2 = NeuralNetworkL(6,2)
print("Weights 1: " + str(NNL2.Weights))
print("Bias's 1: " + str(NNL2.Bias))
L2O = NNL2.Layer(NNL1.ReLU(NNL1.Layer(I)))
print(NNL2.Layer(NNL1.ReLU(NNL1.Layer(I))))
print(NeuralNetworkL.SoftMax(L2O))
