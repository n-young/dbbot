from textgenrnn import textgenrnn

# TODO: prefix?

textgen = textgenrnn(weights_path='./dearblueno_weights.hdf5', vocab_path='./dearblueno_vocab.json', config_path='./dearblueno_config.json', name='dearblueno')
textgen.generate(temperature=1)