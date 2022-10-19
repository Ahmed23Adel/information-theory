import argparse
import huffman as huff

parser = argparse.ArgumentParser()
group_algoithms = parser.add_mutually_exclusive_group()

group_algoithms.add_argument('--huffman',action='store_true')
group_algoithms.add_argument('--shanon-fano',action='store_true')
parser.add_argument('--run-all', action='store_true')
args = parser.parse_args()


if __name__ =='__main__':
    if args.huffman:
        if args.run_all:
            huff.run_huffman()
