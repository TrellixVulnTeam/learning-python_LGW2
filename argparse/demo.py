import argparse

parser = argparse.ArgumentParser(description='命令行中传入一个数字')
parser.add_argument('integers', type=int, nargs='+', help='传入的数字')
parser.add_argument('--abc', '-a', type=int, nargs='+', help='传入的数字')
args = parser.parse_args()

# 对传入的数据进行加总
print(sum(args.integers))

