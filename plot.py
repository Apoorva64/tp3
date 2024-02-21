# 3d plot of the results with size and threads as axis and the time as the value with 2 subplots
import numpy as np
import base64
import pickle
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# load data
data = base64.b64decode("""gASV0wEAAAAAAABdlCh9lChNECdLAYaURz843Qp2allUTRAnSwKGlEc/OgCHOW+4Sk0QJ0sEhpRHPziHqV+93lBNECdLCIaURz+CbZ8/y8fqTRAnSxCGlEc/jnwvJYd5Bk0QJ0sghpRHP5RydxXhEtVKoIYBAEsBhpRHP3HbmkUQKnBKoIYB
AEsChpRHP2TYVD9yW71KoIYBAEsEhpRHP2F/U/McQdVKoIYBAEsIhpRHP3Wt2cJ+lTFKoIYBAEsQhpRHP472gCR9jcpKoIYBAEsghpRHP5lAUFIn6wFKQEIPAEsBhpRHP6pZxxuy4+1KQEIPAEsChpRHP5wxAgCLQDtKQEIPAEsEhpRHP5hZ
/nkXQxNKQEIPAEsIhpRHP5As7nWUANNKQEIPAEsQhpRHP5Ufeu+KZvdKQEIPAEsghpRHP6ESnz71CFVKgJaYAEsBhpRHP+R889wFTvRKgJaYAEsChpRHP9TnuAqd6LRKgJaYAEsEhpRHP8i2hIvrWy1KgJaYAEsIhpRHP8OiL2pQ1rJKgJaYAEsQhpRHP8OUbDMvAXVKgJaYAEsghpRHP8M2BJ7LMcJ1XZQoTRAnSqCGAQBKQEIPAEqAlpgAZV2UKEsBSwJLBEsISxBLIGVlLg==
""")

openmp_results, SIZE_ARRAY, THREADS_ARRAY = pickle.loads(data)


# make a plot by varying the number of threads and the size of the array 2d

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

# Extract data for openmp and no-openmp
x_openmp, y_openmp = zip(*openmp_results.keys())
z_openmp = list(openmp_results.values())

# Reshape data for 3D plotting
x_openmp = np.array(x_openmp).reshape(len(SIZE_ARRAY), len(THREADS_ARRAY))
y_openmp = np.array(y_openmp).reshape(len(SIZE_ARRAY), len(THREADS_ARRAY))
z_openmp = np.array(z_openmp).reshape(len(SIZE_ARRAY), len(THREADS_ARRAY))

# Plotting the openmp results
ax1.set_title('OpenMP')
ax1.set_xlabel('Size')
ax1.set_ylabel('Threads')
ax1.set_zlabel('Time (s)')
# set size in power of 10
ax1.plot_surface(x_openmp, y_openmp, z_openmp, cmap='viridis', edgecolor='k')
plt.show()