import numpy as np
import math

from basic_decorators import *
from plots import *
from basic_funcs import *
def calc_statistics(probs,result):
    '''
        Calculate some statisctis about results and input:
        entropy
        avg length
        eff
    '''
    infos = [math.log2(1/x) for x in probs]
    infos = [f'{item:.3f}' for item in infos]
    
    entropy = -np.sum(np.multiply(probs,np.log2(probs)))
    avg_len = np.sum(np.multiply(probs,np.array([len(x) for x in result])))
    eff = (entropy/avg_len)*100
    infos_diffs = [len(x)-float(y) for (x,y) in zip(result,infos)]
    infos_diffs = [f'{item:.3f}' for item in infos_diffs]
    return infos,infos_diffs,entropy,avg_len,eff



def run_compression_alg(name, func):
    print("Running sample of {} algorithm \n".format(name),"*"*30)
    input = np.array([0.4, 0.3, 0.15, 0.1, 0.05])
    print("The input is:",input)
    
    result = func(input)
    print("The result for inputs is: ",result)
    infos,infos_diffs,entropy,avg_len, eff = calc_statistics(input,result)
    print("information for each elemnt: {}".format(infos))
    print("Incease in each element is: {}".format(infos_diffs))
    print("Entropy= {:.4f} \nAverage length= {:.4f} \n Efficiency= {:.4f}%".format(entropy,avg_len, eff))
    print("*"*30)