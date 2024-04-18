import sys;
import random;
import numpy;



class Neuron:
    def __init__(self, dimension, learnrate):
        self.dimension = dimension
        #self.name = name
        self.inputs = []
        self.weights = []
        self.output = float("NaN")
        self.learnrate = learnrate
        self.weightchanges=[]
        self.error=0
        for i in range(dimension + 1):
            self.weights.append(numpy.random.rand())
            self.weightchanges.append(0)


    def GetOutput(self,inpoint):
        point = self.AddBiasInput(inpoint)
        maxpoint = max(point)
        self.inputs = list(numpy.divide(point,maxpoint))
        self.output = self.EvalFunc()
        print("GETOUTPUT: POINT = {} scaled {},OUTPUT {}".format(point,self.inputs,self.output))
        return self.output
        

    def EvalFunc(self):
        suma = numpy.dot(self.inputs, self.weights)
        print("Point {0} weights {1} suma {2}".format(self.inputs,self.weights,suma))
        return numpy.exp(suma)/(1+numpy.exp(suma))

    def ApplyWeightChange(self):
        for idx in range(len(self.weights)):
            #print("Adjust weights {0} = {1} - {2}*{3}".format(self.weights[idx] - self.learnrate*self.weightchanges[idx],self.weights[idx],self.learnrate,self.weightchanges[idx]))
            self.weights[idx] -= self.learnrate * self.weightchanges[idx]

    def AddBiasInput(self, point):
        biasinput = [1] + point
        return biasinput

    def SaveWeigths(self, filename):
        f = open(filename, "w")
        f.write(";".join((str(x) for x in self.weights)))
        f.close();


class MultiLayerNetwork:
    def __init__(self, dimension, learnrate,layer_definition):
        self.learnrate = learnrate
        self.dimension = dimension
        self.NeuralNetwork = []
        self.inputs=[]
        self.errors=[]
        self.layer_definition = layer_definition
        for l in range(len(layer_definition)):
            self.NeuralNetwork.append([])
            for j in range(layer_definition[l]):
                if l == 0:
                    self.NeuralNetwork[l].append(Neuron(self.dimension,self.learnrate))
                    print("Adding Neuron {0} of dimension {1} in layer {2}".format(j,self.dimension,l))
                else:
                    self.NeuralNetwork[l].append(Neuron(layer_definition[l-1],self.learnrate))
                    print("Adding Neuron {0} of dimension {1} in layer {2}".format(j,layer_definition[l-1],l))
    
    def GetOutput(self,neuron,inpoint):
        return neuron.GetOutput(inpoint)
    
    def Train(self,pointlist,expected,cycles):
        for c in range(cycles):
            for idx in range(len(pointlist)):
                self.inputs = pointlist[idx]
                print("Initial input vector {0}".format(self.inputs))
                #print("Epoch {1} FeedForward {0} START".format(idx,c))
                for layeridx in range(len(self.NeuralNetwork)):
                    outputs=[]
                    for neuron in self.NeuralNetwork[layeridx]:
                        outputs.append(self.GetOutput(neuron,self.inputs))
                    if layeridx<len(self.NeuralNetwork)-1:
                        print("Layer {0}: Inputs {1} generated outputs {2} as input for layer  {3}".format(layeridx,self.inputs,outputs,layeridx+1))
                        self.inputs = outputs

                    else:
                        self.errors = [((1/2) * (expected[idx][neuridx] - outputs[neuridx])**2) for neuridx in range(len(self.NeuralNetwork[layeridx]))]
                        print("Layer {0} is last. Reached errors {1} with outputs {2} should be {3}".format(layeridx,self.errors,outputs,expected[idx]))

                #print("Epoch {1} FeedForward {0} FINISH".format(idx,c))
                #print("Epoch {1} BackPropag {0} START".format(idx,c))

                for layeridx in reversed(range(len(self.NeuralNetwork))):    
                    for neuridx in range(len(self.NeuralNetwork[layeridx])):
                        neuroerror=float("NaN")
                        if layeridx<len(self.NeuralNetwork)-1:
                            errvect=[x.error for x in self.NeuralNetwork[layeridx+1]]
                            outvect=[x.output*(1-x.output) for x in self.NeuralNetwork[layeridx+1]]
                            weightvect=[x.weights[neuridx+1] for x in self.NeuralNetwork[layeridx+1]]
                            #print("(((((((")
                            #for i in range(len(outvect)):
                                #print("{0} * {1} * {2}".format(errvect[i],outvect[i],weightvect[i]),end=" + ")
                                #print("=")
                                #print("[{0}]".format(errvect[i] * outvect[i] * weightvect[i]))
                            
                            #neuroerror=numpy.dot(numpy.dot(errvect,outvect),weightvect)
                            neuroerror=numpy.sum(numpy.multiply(numpy.multiply(errvect,outvect),weightvect))
                            #print(" = {0})))))))".format(neuroerror))
                            #print("Layer {0} Neuron {4}: Error {5}. Outputs of layer {1} are {2}. Weights {3}".format(layeridx, layeridx + 1,outvect, weightvect,neuridx,neuroerror))
                        else:
                            neuroerror = self.NeuralNetwork[layeridx][neuridx].output-expected[idx][neuridx]
                            #print("Layer {0} is last. Neuron {1} has error {2} ({3} - {4})".format(layeridx,neuridx,neuroerror,self.NeuralNetwork[layeridx][neuridx].output,expected[neuridx]))
                        self.NeuralNetwork[layeridx][neuridx].error=neuroerror
                
                        
                        for weightidx in range(len(self.NeuralNetwork[layeridx][neuridx].weights)):
                            #learner=1#self.NeuralNetwork[layeridx][neuridx].learnrate
                            out = self.NeuralNetwork[layeridx][neuridx].output
                            inp = self.NeuralNetwork[layeridx][neuridx].inputs[weightidx]
                            delta = neuroerror*out*(1-out)*inp
                            #print("Layer {0} Neuron {1} delta {2} ({6}) =  {3} * {4} * (1- {4}) * {5}".format(layeridx,neuridx,weightidx,neuroerror,out,inp,delta))
                            self.NeuralNetwork[layeridx][neuridx].weightchanges[weightidx] = delta
                            #print("Layer {0} Neuron {1} Weight {2} ({3}) with input ({4}) gets delta {5} -> {6}".format(layeridx,neuridx,weightidx,
                             #                                                                                         self.NeuralNetwork[layeridx][neuridx].weights[weightidx],
                             #                                                                                         self.NeuralNetwork[layeridx][neuridx].inputs[weightidx],delta,
                              #                                                                                        self.NeuralNetwork[layeridx][neuridx].weights[weightidx]-self.NeuralNetwork[layeridx][neuridx].learnrate*self.NeuralNetwork[layeridx][neuridx].weightchanges[weightidx]))
                            #print("Layer {0} Neuron {1} Weight {2} will be {3}".format(layeridx,neuridx,weightidx,self.NeuralNetwork[layeridx][neuridx].weights[weightidx]-self.NeuralNetwork[layeridx][neuridx].learnrate*self.NeuralNetwork[layeridx][neuridx].weightchanges[weightidx]))

                #print("Epoch {1} BackPropag {0} FINISH".format(idx,c))
                for layeridx in range(len(self.NeuralNetwork)):
                    for neuron in self.NeuralNetwork[layeridx]:
                        neuron.ApplyWeightChange()
                finaloutputs=[x.output for x in self.NeuralNetwork[len(self.NeuralNetwork)-1]]
                print("Epoch {0} Point {1} output {2} expected {3}. Totalerror {4}".format(c,pointlist[idx],finaloutputs,expected[idx],numpy.sum(self.errors)))
                print("__________")
            print("----")
                        
    def Test(self,pointlist):
        finaloutputs=[]
        for idx in range(len(pointlist)):
            self.inputs = pointlist[idx]
            for layeridx in range(len(self.NeuralNetwork)):
                outputs=[]
                for neuron in self.NeuralNetwork[layeridx]:
                    outputs.append(self.GetOutput(neuron,self.inputs))
                if layeridx<len(self.NeuralNetwork)-1:
                    self.inputs = outputs
            finaloutputs.append(outputs)
        return finaloutputs     
                   
              
def main():
    dimension = 5
    learnrate = 0.5
    learncyclecount = 1000000

    layer_definition=[4,3]
   
    testset=trainset = [[0,0],[1,0],[0,1],[1,1]]
    expectedresults = [[0],[1],[1],[0]]
    trainingset = [[0.05,0.10]]
    trainexpect=[[0.01,0.99]]
    trainingset2=[
    [42,100,50,50,50],
    [37,100,100,20,0],[42,0,100,100,100]
    ]
    trainexpect2=[[0,1,0],[1,0,0],[0,0,1]]
    b1=0.35
    b2=0.60
    w1=0.15
    w2=0.20
    w3=0.25
    w4=0.30
    w5=0.40
    w6=0.45
    w7=0.50
    w8=0.55
    
    
    
    
    
    net = MultiLayerNetwork( dimension, learnrate,layer_definition);
    #net.NeuralNetwork[0][0].weights = [b1,w1,w2]
    #net.NeuralNetwork[0][1].weights = [b1,w3,w4]
    #net.NeuralNetwork[1][0].weights = [b2,w5,w6]
    #net.NeuralNetwork[1][1].weights = [b2,w7,w8]
    
    
    
    
    #net.Train(trainset, expectedresults, learncyclecount)
    net.Train(trainingset2, trainexpect2, learncyclecount)
    #results = net.Test(testset)
    #for idx in range(len(results)):
    #    print("{3}. Point {0} has result {1} ({2})".format(testset[idx], results[idx], expectedresults[idx] ,idx))




if __name__ == "__main__":
    main()