import random
import math


class ANNFitting:
    """This class trains the ANN model.

    The training process is made by inputing new information and calculating
    the global difference between the output and the desired output.

    Focused on:
        Optimization Method: SGD (Stochastic Gradient Descent).
        - Propagation and Backpropagation algorithms.

    """
    def __init__(self, data, labels, activation_function='sigmoide', hidden_layers=1, neurons=3):
        self.data = data
        self.labels = labels

        self.functions = {
            'sigmoide': ['', ''],
            'relu': ['', ''],
            'tanh': ['', '']
        }

        self.activation_function = self.getting_activation(activation_function)

        self.input_layer_len = self.defining_input_layer()
        self.output_layer_len = self.defining_output_layer()
        self.hidden_layers = [[]] * hidden_layers
        self.neurons = [[]] * neurons

        self.synaptic_weights = (hidden_layers + 1) * [[]]

        self.lengths = [
            self.input_layer_len,
            self.output_layer_len
        ]

    # Used in __init__
    def getting_activation(self, function):
        """This function returns the chosen activation function and it
        respectively derivative.

        Parameters
        ----------
        function : str
            The activation function's name.
        Returns
        -------
        self.functions.get(function) : list
            List with the activation function and it respectively derivative.

        """
        return self.functions.get(function)

    # Used in __init__
    def defining_input_layer(self):
        """This function, given a dataset, returns the input layer length.

        Returns
        -------
        len(self.data.columns) : int
            Input layer length.

        """
        return len(self.data.columns)

    # Used in __init__
    def defining_output_layer(self):
        """This function, given a dataset, returns the output layer length.

        Returns
        -------
        len(self.lables.unique()) : int
            Output layer length.

        """
        return len(self.labels.unique())

    # Used in __call__
    def defining_hidden_layers(self):
        """This function defines the array structure of the hidden layers.

        Returns
        -------
        none : None
            This function has no return.

        """
        for i in range(len(self.hidden_layers)):
            self.hidden_layers[i] = self.neurons

    # Used in __call__
    def defining_hidden_layers_len(self, list_len):
        """This function defines the length of the available hidden layers.

        Parameters
        ----------
        list_len : lst
            List with all the hidden layers length.

        Returns
        -------
        none : None
            This function has no return.

        """
        for idx in range(len(list_len)):
            self.lengths.insert((idx + 1), list_len[idx])

    # Used in __call__
    def defining_synaptic_weights(self):
        """This function defines the synaptic weights length.

        Returns
        -------
        list_len : list
            list with the lengths of the synaptic weights.

        """
        list_len = []
        for hidden_layer_neurons in self.hidden_layers:
            list_len.append(len(hidden_layer_neurons))

        return list_len

    # Used in __call__
    def generating_synaptic_weights(self):
        """This function generates the synaptic weights structure.

        Returns
        -------
        synaptic_list : list
            List with all the synaptic weights lengths.

        """
        list_len = len(self.lengths) - 1
        synaptic_list = []
        for index, elem in enumerate(self.lengths):
            if index == list_len:
                pass
            else:
                synaptic_list.append(elem * self.lengths[self.lengths.index(elem) + 1])

        return synaptic_list

    # Used in __call__
    def randomizing_synaptic_weights(self, synaptic_list):
        """This function, by randomizing it, generates all the synaptic weights.

        Parameters
        ----------
        synaptic_list : list
            List with all the synaptic weights lengths.

        Returns
        -------
        none : None
            This function has no return.

        """
        for idx, layer in enumerate(synaptic_list):
            self.synaptic_weights[idx].append(random.random())

    def __call__(self, *args, **kwargs):
        self.defining_hidden_layers()

        synaptic_weights_list = self.defining_synaptic_weights()

        self.defining_hidden_layers_len(synaptic_weights_list)

        self.randomizing_synaptic_weights(self.generating_synaptic_weights())

        pass


if __name__ == '__main__':
    import pandas

    df = pandas.read_csv('../docs/iris.csv')

    train = df.iloc[:, 0: -1]
    test = df.iloc[:, -1]

    obj = ANNFitting(data=train, labels=test)
    obj()

    """
    def test_(row):
        print(row)

    train.apply(lambda row: test_(row), axis=1)
    test.apply(lambda row: test_(row))
    """
