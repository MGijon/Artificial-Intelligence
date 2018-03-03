import logging
import pandas as pd
import gensim.models as gm

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# ruta mac:
filepath = 'Data/words_source_v2.csv'
# ruta windows:
# filepath = ''
data = pd.read_csv(filepath, sep = ';')
logger.info('File imported')

# ruta mac:
route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
# ruta windows:
# route = 'D:\GIT\Data\GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)
logging.info('Model upload, starting with the process')

i = 0

while isinstance(data['Pos1'][i] , str):

    #if isinstance(data['R2'][i] , str) == False:

    resultado = model.most_similar( positive = [data['Pos1'][i], data['Pos2'][i]],
                                    negative = [data['Neg'][i]], topn = 5)
    data['R1'][i] = resultado[0][0]
    data['R2'][i] = resultado[1][0]
    data['R3'][i] = resultado[2][0]
    data['R4'][i] = resultado[3][0]
    data['R5'][i] = resultado[4][0]

    i = i + 1

logging.info('Process finished')
filepath = 'Data/words_source_v2.2.csv'
data.to_csv(filepath, sep = ';', index = False)
