import math
import random
import time
import os


class BaseSolver(object):
    def __init__(self, matrix=[]):
        self.matrix = matrix
        self.route = []
        self.size = len(matrix)
        self.sol = float('inf')
        self.trace = []
        self.start = 0

        return

    def read_data(self, filename):
        coordinates = []
        with open(filename, 'r') as infile:
            lines = infile.readlines()
            idx = 5
            while lines[idx].strip() != 'EOF':
                coordinates.append(
                    list(map(float, lines[idx].strip().split()[-2:])))
                idx += 1

        n = len(coordinates)
        self.size = n
        self.matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                self.matrix[i][j] = round(
                    math.dist(coordinates[i], coordinates[j]))
        return

    def solve(self, cutoff, seed):
        random.seed(seed)
        self.start = time.time()
        return

    def write_solution(self, filename):
        with open(filename, 'w') as outfile:
            outfile.write(str(self.sol) + '\n')
            outfile.write(','.join([str(v) for v in self.route]))
        return

    def init_trace(self, filename):
        if os.path.exists(filename):
            os.remove(filename)
        self.trace_file = open(filename, 'a')
        return

    def record_trace(self):
        self.trace_file.write(
            str(time.time() - self.start) + ',' + str(self.sol) + '\n')