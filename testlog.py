import logging
import numpy as np

def logger(parameter):
    logging.basicConfig(format='%(asctime)s %(message)s')
    logging.warning(np.eye(parameter))
    return 
