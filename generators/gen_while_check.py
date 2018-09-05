import os
import psutil


def memory_usage():
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0] / float(2 ** 20)
    return mem


def next_cubes(n):
    i = 1
    while i <= n:
        yield i**3
        i += 1

if __name__ == '__main__':
    res = next_cubes(1000000)
    next(res)
    print memory_usage()
