import random


class ANNFitting:
    def __init__(self, data, labels, activation_function='sigmoide', hidden_layers=1, neurons=3):
        self.data = data
        self.labels = labels
        self.activation_function = activation_function

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
    def defining_input_layer(self):
        return len(self.data.columns)

    # Used in __init__
    def defining_output_layer(self):
        return len(self.labels.unique())

    # Used in __call__
    def defining_hidden_layers(self):
        for i in range(len(self.hidden_layers)):
            self.hidden_layers[i] = self.neurons

    # Used in __call__
    def defining_hidden_layers_len(self, list_len):
        for idx in range(len(list_len)):
            self.lengths.insert((idx + 1), list_len[idx])

    # Used in defining_lengths
    def defining_synaptic_weights(self):
        list_len = []
        for hidden_layer_neurons in self.hidden_layers:
            list_len.append(len(hidden_layer_neurons))

        return list_len

    # Used in __call__
    def generating_synaptic_weights(self):
        list_len = len(self.lengths) - 1
        list_ = []
        for index, elem in enumerate(self.lengths):
            if index == list_len:
                pass
            else:
                list_.append(elem * self.lengths[self.lengths.index(elem) + 1])

    def __call__(self, *args, **kwargs):
        self.defining_hidden_layers()
        self.defining_synaptic_weights()
        self.defining_hidden_layers_len(self.defining_synaptic_weights())

        print('')


if __name__ == '__main__':
    import pandas

    df = pandas.read_csv('../docs/iris.csv')

    train = df.ix[:, 0: -1]
    test = df.ix[:, -1]

    obj = ANNFitting(data=df.ix[:, 0: -1], labels=df.ix[:, -1])
    obj()

    """
    def test_(row):
        print(row)

    train.apply(lambda row: test_(row), axis=1)
    test.apply(lambda row: test_(row))
    """
