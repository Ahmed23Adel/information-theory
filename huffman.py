from audioop import reverse
from re import L
import numpy as np
from basic_decorators import *
from plots import *
from Algorithm import *


class Huffman(Algorithm):

    def __init__(self):
        self.name = "Huffman"
        

    def run_algoirthm(self,probs,original_length,codes=None):
        '''
        It performs Huffman compression algorithm by recursion
        '''
        if len(probs) == 1: return # Break the recursion
        sorted = (probs ==np.sort(probs)).all() # if not sorted it will reverse between 0 and 1 whilte appending new element for the code
        probs = np.sort(probs)[::-1] # sorting the algoirhtms first
        
        codes = ['']*len(probs) if codes == None else codes # intialize the codes for the first time only
        trunc_lst = probs[:-1] # truncate the last element of probs as it will be summed to the next level
        diff = original_length - len(trunc_lst) # to add ex 1 to all prev states
        if not sorted:
            codes[-diff:] = [x+'1' for x in codes[-diff:]]
            codes[-diff-1] = codes[-diff-1] + '0' # last index only has zero, but all below will have 1
        else:
            codes[-diff:] = [x+'0' for x in codes[-diff:]]
            codes[-diff-1] = codes[-diff-1] + '1'

        trunc_lst[-1] = sum(probs[-2:]) # sum last two elements of probs into one in trunc_lst
        self.run_algoirthm(trunc_lst,original_length = original_length, codes = codes) # I'm assuming that I work with list which is mutable
        codes = [x[::-1] for x in codes]
        return codes

    # @checkProbs1 # you must call checkProbls before checkSize as checksize doesn't call checkProbls1 if size =2
    # @checkSize  
    def _run_alorithm(self,probs):
        return self.run_algoirthm(probs,len(probs))

    





