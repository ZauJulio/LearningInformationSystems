import subprocess
import platform
import sys
import random
import os

import matplotlib.pyplot as plt
import numpy as np


class Compare:
    def __init__(self, n_iter, numbers):
        """  """
        self.n_iter = n_iter
        self.numbers = numbers

        # List of algorithms id's
        self.algorithms = [
            "bubbleSort",
            "selectionSort",
            "insertionSort",
            "quickSort"
        ]

        # List of algorithms modules
        self.build_name = "_".join([
            "sort",
            "x"+platform.architecture()[0][:-3],
            platform.system().title()
        ])

        # Chronometer module
        self.chronos = "chronometer"+self.build_name[4:]+".so"

        # Init stucture
        self.c, self.go = {}, {}
        for alg in self.algorithms:
            self.c[alg] = []
            self.go[alg] = []

    def buildDependencies(self) -> None:
        """  """
        print("compiling...", end="  ")

        if "../std/"+self.build_name+"_c.so" not in os.listdir('../std/'):
            # Build C version
            compile_c = subprocess.run([
                "gcc", "-o",
                "../std/"+self.build_name+"_c.so",
                "../std/sort.c"
            ])

        if "../std/"+self.build_name+"_go.so" not in os.listdir('../std/'):
            # Build Go version
            compile_go = subprocess.run([
                "go", "build", "-o",
                "../std/"+self.build_name+"_go.so",
                "../std/sort.go"
            ])

        if self.chronos not in os.listdir():
            # Build chronometer
            compile_go = subprocess.run([
                "gcc", "-o", self.chronos, "chronometer.c"
            ])

        print("Done")

    def run(self):
        """  """
        numbers = str(self.numbers)[1:-1].replace(',', '')

        for i in range(self.n_iter):
            for alg in self.algorithms:
                t_c = subprocess.run(
                    args=[
                        "./"+self.chronos, "../std/"+self.build_name+"_c.so",
                        alg,
                        numbers
                    ],
                    universal_newlines=False,
                    stdout=subprocess.PIPE
                )

                t_go = subprocess.run(
                    args=[
                        "./"+self.chronos, "../std/"+self.build_name+"_go.so",
                        alg,
                        numbers
                    ],
                    universal_newlines=False,
                    stdout=subprocess.PIPE
                )

                self.c[alg].append(float(str(t_c.stdout).split("\\n")[1]))
                self.go[alg].append(float(str(t_go.stdout).split("\\n")[1]))

    def plot(self):
        """  """
        pass
        # c_means, go_means = [], []
        # x1, x2, y1, y2 = [], [], [], []
        # labels = {'x':[], 'labels':[]}

        # for i in self.c.keys():
        #     c_means.append([sum(self.c[i])/len(self.c[i])])

        # for i in self.go.keys():
        #     go_means.append([sum(self.go[i])/len(self.go[i])])

        # for i, alg in enumerate(self.algorithms):
        #     x1.append(i+1)
        #     x2.append(i+.5)

        #     y1.append(c_means[i][0])
        #     y2.append(go_means[i][0])

        #     labels['x'].append(i)
        #     labels['x'].append(i)
            
        #     labels['labels'].append(alg)
        #     labels['labels'].append(alg)

        # p1 = plt.bar(x1, y1, width=0.5)
        # p2 = plt.bar(x2, y2, width=0.5)
        
        # plt.xticks(labels['x'], labels['labels'])
        # plt.legend((p1[0], p2[0]), ('C', 'Go'))

        # plt.xlabel('Milliseconds')
        # plt.ylabel('Algorithms')

        # plt.title("Milliseconds comparison of ordering algorithms in C and Go")
        # plt.legend()
        # plt.show()


if __name__ == "__main__":
    args = sys.argv[1:]

    n_iter = int(args[0])
    numbers = random.sample(range(100), int(args[1]))

    cmp = Compare(n_iter, numbers)
    cmp.run()
    cmp.plot()

