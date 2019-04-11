class ANNFitting:
    def __init__(self, data, labels, activation_function='sigmoide', hidden_layers=1, neurons=3):
        self.data = data
        self.labels = labels
        self.activation_function = activation_function

        self.input_layer_len = self.defining_input_layer()
        self.output_layer_len = self.defining_output_layer()
        self.hidden_layers = [[]] * hidden_layers
        self.neurons = [[]] * neurons

        self.synaptic_weights = hidden_layers * [[]]

    def defining_synaptic_weights(self):
        pass

    def defining_input_layer(self):
        return len(self.data.columns)

    def defining_output_layer(self):
        return len(self.labels.unique())

    def defining_hidden_layers(self):
        for i in range(len(self.hidden_layers)):
            self.hidden_layers[i] = self.neurons


if __name__ == '__main__':
    import pandas

    df = pandas.read_csv('../docs/iris.csv')

    train = df.ix[:, 0: -1]
    test = df.ix[:, -1]

    ANNFitting(data=df.ix[:, 0: -1], labels=df.ix[:, -1]).defining_hidden_layers()

    # def test_(row):
    #     print(row)

    # train.apply(lambda row: test_(row), axis=1)
    # test.apply(lambda row: test_(row))

