import argparse

parser = argparse.ArgumentParser(description='test description')
parser.add_argument('arg1', type=str, help='test help')
args = parser.parse_args()
print(type(args.arg1))
print(args.arg1)
