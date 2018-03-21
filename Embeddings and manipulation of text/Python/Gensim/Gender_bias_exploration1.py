import numpy as np
import pandas as pd
import gensim.models as gm
import matplotlib.pyplot as plt
import logging

# create logger
logger = logging.getLogger('report_Gender_bias_debiation')
logger.setLevel(logging.DEBUG)
# create file handler
fh = logging.FileHandler('report_Gender_bias_debiation.log')
fh.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)

# ruta mac:
route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
# ruta windows:
# route = 'D:\GIT\Data\GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)
logger.info('Model loaded successfully')

total_size = len(model.wv.vocab)
threshold = 0.25
logger.info('Total size of vocabulary: %s\nThreshold fixed at %s\n', total_size, threshold)

#print(model.most_similar( positive = ['woman', 'doctor'], negative = ['man'], topn = 1))
