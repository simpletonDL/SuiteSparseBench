import pytest

from loader import *
from pygraphblas import *


def real_add(pathA, pathB, tp=float):
    A = load_mtx(pathA, tp)
    B = load_mtx(pathB, tp)
    print(A.shape, A.nvals)
    print(B.shape, B.nvals)


@pytest.mark.parametrize(
    "path,tp",
    [
        # ('data/small/b2_ss.mtx', 'data/small/b_dyn.mtx', float),
        # ('data/small/fs_760_2.mtx', 'data/small/fs_760_3.mtx', float),
        # ('data/medium/NotreDame_www.mtx', 'data/medium/web-NotreDame.mtx', bool),
        # ('data/small/arc130.mtx', float),
        ('data/fixed_set/linux_call_graph.mtx', float),
        ('data/fixed_set/webbase-1M.mtx', float)
    ]
)
def test_EWiseAdd(path, tp, benchmark):
    print(f'Loading matrix {path} with type {tp}...')

    A = load_mtx(path, tp)
    print(f'Transpose matrix...')
    A_T = A.transpose()

    def add():
        C = A + A_T
        return C

    print('Start benchmarking A + A+T')
    res: Matrix = benchmark(add)
    print(f'\n'
          f'A: {A.shape, A.nvals, A.type},\n'
          f'A + A_T: {res.shape, res.nonzero().nvals, res.type}\n')
