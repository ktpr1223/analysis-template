import os
import yaml


def prep():
    path = os.path.dirname(os.path.abspath(__file__))
    print(
        yaml.load(open(os.path.join(path.split('src')[0], 'config/prep.yml'))))
    return 2
