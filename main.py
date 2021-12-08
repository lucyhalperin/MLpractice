import argparse
parser = argparse.ArgumentParser(description='testparse')
parser.add_argument("--hyperparamX", type=int, default=3,
        help="some hyperparameter")
args = parser.parse_args()

print(args.hyperparamX)





