import numpy as np
import math
from basic_decorators import *
from plots import *

class Algorithm(object):
    
    def __inif__(self):
        self.name = None
    
    def run_algoirthm(self, probs):
        raise NotImplementedError

    # @checkProbs1 # you must call checkProbls before checkSize as checksize doesn't call checkProbls1 if size =2
    # @checkSize  
    def _run_alorithm(self,probs):
        raise NotImplementedError


    def __run(self,input):
        print("Running sample of {} algorithm \n".format(self.name),"*"*30)
        print("The input is:",input)
        
        result = self._run_alorithm(input)
        print("The result for inputs is: ",result)
        infos,infos_diffs,entropy,avg_len, eff = self.calc_statistics(input,result)
        print("information for each elemnt: {}".format(infos))
        print("Incease in each element is: {}".format(infos_diffs))
        print("Entropy= {:.4f} \nAverage length= {:.4f} \n Efficiency= {:.4f}%".format(entropy,avg_len, eff))
        print("*"*30)

    def run_sample(self):
        self.__run(np.array([0.4, 0.3, 0.15, 0.1, 0.05]))


    def run_eng_letters(self):
        self.__run(self._get_eng_freq())


    def calc_statistics(self,probs,result):
        '''
        Calculate some statisctis about results and input:
        entropy
        avg length
        eff
        '''
        infos = [math.log2(1/x) for x in probs]
        infos = [f'{item:.3f}' for item in infos]
        
        entropy = -np.sum(np.multiply(probs,np.log2(probs)))
        print("entropyentropy", entropy)
        avg_len = np.sum(np.multiply(probs,np.array([len(x) for x in result])))
        eff = (entropy/avg_len)*100
        infos_diffs = [len(x)-float(y) for (x,y) in zip(result,infos)]
        infos_diffs = [f'{item:.3f}' for item in infos_diffs]
        return infos,infos_diffs,entropy,avg_len,eff


    

    def _get_eng_freq(self):
        return np.array([12.02,9.10,8.12,7.68,7.31,6.95,6.28,6.02,5.92,4.32,3.98,2.88,2.71,2.61,2.30,2.11,2.09,2.03,1.82,1.49,1.11,0.69,0.17,0.11,0.10,0.07])/100

        