from src.lib_a import hoge
from src.preprocess.prep import prep


def main():
    print(hoge())
    res = prep()
    print(res)


if __name__ == '__main__':
    main()
