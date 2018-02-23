import logging
import pandas as pd
import gensim.models as gm

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

filepath = 'Data/Ofensivas.csv'
data = pd.read_csv(filepath, sep = ';')
logger.info('File imported')

route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)
logging.info('Model upload, starting with the process')

i = 0

while isinstance(data['Pos1'][i] , str):

    if isinstance(data['R2'][i] , str) == False:

        resultado = model.most_similar( positive = [data['Pos1'][i], data['Pos2'][i]],
                                        negative = [data['Neg'][i]], topn = 10)
        data['R1'][i] = resultado[0]
        data['R2'][i] = resultado[1]
        data['R3'][i] = resultado[2]
        data['R4'][i] = resultado[3]
        data['R5'][i] = resultado[4]
        data['R6'][i] = resultado[5]
        data['R7'][i] = resultado[6]
        data['R8'][i] = resultado[7]
        data['R9'][i] = resultado[8]
        data['R10'][i] = resultado[9]

    i = i + 1

logging.info('Process finished')
data.to_csv(filepath, sep = ';')
