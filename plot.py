# 3d plot of the results with size and threads as axis and the time as the value with 2 subplots
import numpy as np
import base64
import pickle
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# load data
data = base64.b64decode("""gASVqgUAAAAAAABdlCh9lChLCksBhpRHPuVJPWCznv5LCksChpRHPwfrA0OsUi5LCksEhpRHPyHIOqgCzyNLCksIhpRHPy2gcUaLogJLCksQhpRHP0AsoBN9raJLCksghpRHP3DcAyCb1uFLZEsBhpRHPuUeSkLvPeZLZEsChpRHPwgfW4/zqIRLZEsEhpRHPxsBFd0/lEhLZEsIhpRHPy2lLHTTELRLZEsQhpRHP0XprACkaq5LZEsghpRHP3tmmz+MBwpN6ANLAYaURz72/OkWptfoTegDSwKGlEc/EQ6jumJvlE3oA0sEhpRHPyR+1uRslW5N6ANLCIaURz8wONBesEIwTegDSxCGlEc/PCxGBBtCp03oA0sghpRHP4N76IO3hRJNECdLAYaURz8r30hpPyKZTRAnSwKGlEc/LAGTUwOIIE0QJ0sEhpRHPymIgQdAVPRNECdLCIaURz8z28PPZvTFTRAnSxCGlEc/PtMUZJD5N00QJ0sghpRHP4r0kuRzsn9KoIYBAEsBhpRHP2WslPPteBNKoIYBAEsChpRHP1gSu5lzrvlKoIYBAEsEhpRHP1Ka14c68kRKoIYBAEsIhpRHP0nWQg3j5bpKoIYBAEsQhpRHP0+t9IlDJAZKoIYBAEsghpRHP40Z+aZJq0VKQEIPAEsBhpRHP58iHw65AGdKQEIPAEsChpRHP4945BdsLVBKQEIPAEsEhpRHP4ObQrwSP3NKQEIPAEsIhpRHP3jov0anWUtKQEIPAEsQhpRHP3UhLHV+3StKQEIPAEsghpRHP5dEGF3E1zVKgJaYAEsBhpRHP9k8bJfYzzpKgJaYAEsChpRHP8pbyH2ys0ZKgJaYAEsEhpRHP79j5KvmozhKgJaYAEsIhpRHP8IUeuFHrhRKgJaYAEsQhpRHP8FmL9/BnBdKgJaYAEsghpRHP8Hy5I6Kcd51fZQoSwpLAYaURz7C/ecpou82SwpLAoaURz67kKGavFDLSwpLBIaURz65YkkXw2KNSwpLCIaURz7GWws+d4n6SwpLEIaURz66Y/vKXakgSwpLIIaURz69bV9lJoaOS2RL
AYaURz7F76t0DJc9S2RLAoaURz7FWViL3UNoS2RLBIaURz7GyJDKX4GSS2RLCIaURz7GRZGvlVluS2RLEIaURz7Dq9liMXhzS2RLIIaURz7FLmVuGOJPTegDSwGGlEc+8DiyThtr7E3oA0sChpRHPvgUnsiCkD5N6ANLBIaURz7vtXz5+68N
TegDSwiGlEc+70odL5C8UE3oA0sQhpRHPvcCR3pfZAtN6ANLIIaURz7wO6Y4J1KZTRAnSwGGlEc/KVO5D6uZoU0QJ0sChpRHPymEx4urgIhNECdLBIaURz8pR/H+gfMBTRAnSwiGlEc/LlWrgyYPtE0QJ0sQhpRHPyl0AJQKyppNECdLIIaU
Rz8p+SVwUfeZSqCGAQBLAYaURz9kHe8pQxpcSqCGAQBLAoaURz9kU4mU6bGKSqCGAQBLBIaURz9jjjzEK5OCSqCGAQBLCIaURz9jmEMCXikrSqCGAQBLEIaURz9j+OYFWAOiSqCGAQBLIIaURz9kCTbgZt2FSkBCDwBLAYaURz+dgsEQAChE
SkBCDwBLAoaURz+ctcikSSAFSkBCDwBLBIaURz+h2Pkq+ajOSkBCDwBLCIaURz+gn82QQStDSkBCDwBLEIaURz+e6XIfAU0HSkBCDwBLIIaURz+eWwXgE9FuSoCWmABLAYaURz/Wxz7uUliSSoCWmABLAoaURz/X38GcFyJbSoCWmABLBIaURz/WikO7QLNOSoCWmABLCIaURz/Xw6hg3LmqSoCWmABLEIaURz/X2FWXC0ngSoCWmABLIIaURz/V4Ajps41hdV2UKEsKS2RN6ANNECdKoIYBAEpAQg8ASoCWmABlXZQoSwFLAksESwhLEEsgZWUu
""")

openmp_results, no_openmp_results, SIZE_ARRAY, THREADS_ARRAY = pickle.loads(data)


# make a plot by varying the number of threads and the size of the array

fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

# Extract data for openmp and no-openmp
x_openmp, y_openmp = zip(*openmp_results.keys())
z_openmp = list(openmp_results.values())

x_no_openmp, y_no_openmp = zip(*no_openmp_results.keys())
z_no_openmp = list(no_openmp_results.values())

# Reshape data for 3D plotting
x_openmp = np.array(x_openmp).reshape(len(SIZE_ARRAY), len(THREADS_ARRAY))
y_openmp = np.array(y_openmp).reshape(len(SIZE_ARRAY), len(THREADS_ARRAY))
z_openmp = np.array(z_openmp).reshape(len(SIZE_ARRAY), len(THREADS_ARRAY))

x_no_openmp = np.array(x_no_openmp).reshape(len(SIZE_ARRAY), len(THREADS_ARRAY))
y_no_openmp = np.array(y_no_openmp).reshape(len(SIZE_ARRAY), len(THREADS_ARRAY))
z_no_openmp = np.array(z_no_openmp).reshape(len(SIZE_ARRAY), len(THREADS_ARRAY))

# Plotting the openmp results
ax1.set_title('OpenMP')
ax1.set_xlabel('Size')
ax1.set_ylabel('Threads')
ax1.set_zlabel('Time (s)')
# set size in power of 10
ax1.plot_surface(x_openmp, y_openmp, z_openmp, cmap='viridis', edgecolor='k')

# Plotting the no-openmp results
ax2.set_title('No OpenMP')
ax2.set_xlabel('Size')
ax2.set_ylabel('Threads')
ax2.set_zlabel('Time (s)')
ax2.plot_surface(x_no_openmp, y_no_openmp, z_no_openmp, cmap='viridis', edgecolor='k')

plt.show()