import matplotlib.pyplot as plt
# make a plot by varying the number of threads and the size of the array
SIZE_ARRAY = [ 10000, 100000, 1000000, 10000000]
THREADS_ARRAY = [1, 2, 4, 8, 16, 32]

EXEC_PATH_OPENMP= "cmake-build-debug/tp3_openmp"
EXEC_PATH_NO_OPENMP= "cmake-build-debug/tp3"

# run with subprocess
import subprocess
from pathlib import Path


def run_solver(exec_path: str, size: int, threads: int ) -> float:
    print(exec_path, size, threads)
    result = subprocess.run([exec_path, str(size), str(threads)], capture_output=True)
    return float(result.stdout.decode("utf-8"))



# openmp
openmp_results = {}
for size in SIZE_ARRAY:
    for threads in THREADS_ARRAY:
        openmp_results[(size, threads)] = run_solver(EXEC_PATH_OPENMP, size, threads)

data = [openmp_results, SIZE_ARRAY, THREADS_ARRAY]

# store in base64
import base64
import pickle
data = pickle.dumps(data)
print(base64.b64encode(data).decode("utf-8"))
