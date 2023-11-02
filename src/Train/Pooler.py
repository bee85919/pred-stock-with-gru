from multiprocessing import Pool
from .Train import Train

class Pooler:
    def __init__(self, syms, pnum=8):
        size = len(syms)
        task = [(i, sym, size) for i, sym in enumerate(syms, start=1)]
        with Pool(processes=pnum) as p:
            p.starmap(Train, task)