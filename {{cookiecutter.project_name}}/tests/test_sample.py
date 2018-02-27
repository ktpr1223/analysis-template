from src.lib_a import hoge
from src.lib_b import fuga
from src.preprocess.prep import prep


def test_hoge():
    assert hoge() == 1


def test_fuga():
    assert fuga() == 3


def test_prep():
    assert prep() == 2
