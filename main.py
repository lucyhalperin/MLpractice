import argparse
from testlog import logger

parser = argparse.ArgumentParser(description='testparse')
parser.add_argument("--hyperparamX", type=int, default=3,
        help="some hyperparameter")
args = parser.parse_args()

logger(args.hyperparamX)


# TODO use the tensorboard
