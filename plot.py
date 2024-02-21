# 3d plot of the results with size and threads as axis and the time as the value with 2 subplots
import numpy as np
import base64
import pickle
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# load data
data = base64.b64decode("""gASVRAIAAAAAAABdlCh9lChNECdLAYaURz833LOoQS/UTRAnSwKGlEc/NRr8JyTUbU0QJ0sEhpRHP0S2YWGq+/5NECdLCIaURz9PB96B5zGOTRAnSxCGlEc/iCc+Mmq2V00QJ0sghpRHP5N1jHQXKRFKoIYBAEsBhpRHP2qElfxWJ1RKoIYB
AEsChpRHP2Q9SWGd1L1KoIYBAEsEhpRHP1i5v/+01oxKoIYBAEsIhpRHP1xdrrHZrFlKoIYBAEsQhpRHP4/EwWWQfZFKoIYBAEsghpRHP5SA6Mir1dxKQEIPAEsBhpRHP6bBj4HoouxKQEIPAEsChpRHP5b9lBT1WotKQEIPAEsEhpRHP5Hc
6ygBpslKQEIPAEsIhpRHP4kYNKoruBVKQEIPAEsQhpRHP5aFGNkU2axKQEIPAEsghpRHP5ssTjyj9T1KgJaYAEsBhpRHP9/TQVsUIs1KgJaYAEsChpRHP9FHz6JqIrRKgJaYAEsEhpRHP8dlum78Nx5KgJaYAEsIhpRHP8JLIxQBPsRKgJaY
AEsQhpRHP8XffoA4n4RKgJaYAEsghpRHP8SquKXOW0JKAOH1BUsBhpRHQBgQOvt+kQBKAOH1BUsChpRHQAobz9S/CZZKAOH1BUsEhpRHP//fhMrVe8hKAOH1BUsIhpRHP/sZb6guh9NKAOH1BUsQhpRHP/ky1NQCSzRKAOH1BUsghpRHP/iinHeaa1F1XZQoTRAnSqCGAQBKQEIPAEqAlpgASgDh9QVlXZQoSwFLAksESwhLEEsgZWUu""")

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