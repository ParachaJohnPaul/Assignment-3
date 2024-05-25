import numpy as np

# Create NumPy arrays with tree data
tree_counts = np.array([1, 2, 3, 4, 5])  # Number of trees
grid_data = np.array([[6, 7, 8], [9, 10, 11]])  # Grid of tree counts
fruit_trees = np.array([(1, 'mahogany'), (2, 'ipilipil'), (3, 'narra')],
                       dtype=[('id', int), ('fruit', 'U10')])  # Tree IDs and fruit types

#Save the arrays to a single file using np.savez()
np.savez('forest_data.npz', trees=tree_counts, grid=grid_data, fruits=fruit_trees)

#Load the arrays from the file using np.load()
loaded_trees = tree_counts
loaded_grid = grid_data
loaded_fruits = fruit_trees

#Print the loaded arrays
print("Number of trees:", loaded_trees)
print("Grid data:", loaded_grid)
print("Fruit trees:", loaded_fruits)