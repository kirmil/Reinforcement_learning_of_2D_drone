import numpy as np
class dense_model():
    import random
    def __init__(self):
        self.input_Size = []
        self.model = []
        self.model_size_vals = []
        self.weights = []
        self.bias = []
# Man ska kunna skapa model med input_size, 
# Man ska kunna lägga till dense lager och ReLu lager, och tillsist output size.
# Man ska kunna skapa loss function
# Man ska kunna träna modell
    def add_input_layer(self,size):
        self.model.append("i"+str(int(size)))
        self.model_size_vals.append(int(size))
    def add_dense_layer(self,size):
        self.model.append("d"+str(int(size)))
        self.model_size_vals.append(int(size))
    def add_relu(self):
        self.model.append("r")
    def add_Output(self,size):
        self.model.append("o"+str(int(size)))
        self.model_size_vals.append(int(size))
    def compile_network(self):
        prev_size = 0
        count = 0
        for i in self.model:
            if i[0] != "r":
                if i[0]=="i":
                    pass
                elif i[0] == "d" or i[0]=="o":
                   
                    self.weights.append( np.random.uniform(low=-1, high=1, size=(self.model_size_vals[count],prev_size)))
                    self.bias.append( np.random.uniform(low=-1, high=1, size=(self.model_size_vals[count],1)))
                prev_size = self.model_size_vals[count]
                count = count+1
    def predict(self,input_vect):
        count_dense = 0
        current_neuron_val = input_vect
        for i in self.model:
            if i[0] == "i":
                pass
            if i[0]=="r":
                
                for v in range(0,len(current_neuron_val)):
                    if current_neuron_val[v]<0:
                        current_neuron_val[v]=0
                
            if i[0] =="d" or i[0]=="o":
                current_neuron_val = np.matmul(self.weights[count_dense],current_neuron_val)+self.bias[count_dense]
                current_neuron_val = 1/(1+np.exp(-current_neuron_val))
                count_dense = count_dense+1
        return current_neuron_val

    def uppdate_Model():
        pass
    def calculate_Loss():
        pass
    pass

test = dense_model()
test.add_input_layer(5)
test.add_dense_layer(4)
test.add_dense_layer(3)
test.add_relu()
test.add_Output(8)
test.compile_network()
a = np.array([[1],[2],[3],[4],[5]]) 


