import argparse
import huffman as huff
from huffman import *
parser = argparse.ArgumentParser()
group_algoithms = parser.add_mutually_exclusive_group()

group_algoithms.add_argument('--huffman',action='store_true')
group_algoithms.add_argument('--shanon-fano',action='store_true')
parser.add_argument('--run-sample', action='store_true')
parser.add_argument('--run-eng', action='store_true')
args = parser.parse_args()


if __name__ =='__main__':
    alg = Huffman()
    if args.huffman:
        if args.run_sample:
            alg.run_sample()
        elif args.run_eng:
            alg.run_eng_letters()
