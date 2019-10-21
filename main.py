from algorithm import TrialAndError
import numpy as np
from io import StringIO

def main():
    file = open("p01_d.txt", 'r')
    content = StringIO(f"{file.read()}")

    distances = np.loadtxt(content, dtype = int)
    algorithm = TrialAndError(distances)

    print(algorithm.commit())

if __name__ == "__main__":
    main()