from pygraphblas import *


def load_mtx(path, tp):
    with open(path, 'r') as f:
        xs = map(lambda s: s.strip().split(), filter(lambda s: not s.startswith('%'), f))
        n, m, nnz = [int(x) for x in next(xs)]

        if tp == bool:
            I, J = zip(*xs)
            V = [True] * len(I)
        else:
            I, J, V = zip(*xs)
            V = [tp(x) for x in V]

        I, J = [[int(x) for x in xs] for xs in (I, J)]

        mtx = Matrix.from_lists(I, J, V, nrows=n+1, ncols=m+1)
    return mtx



# load_mtx('data/Trec4.mtx', int)
