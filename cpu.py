import os


def set_omp_num_threads(num: int):
    os.environ["OMP_NUM_THREADS"] = str(num)
