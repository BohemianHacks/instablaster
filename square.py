import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
  """Creates a white image with a black square at specified coordinates.

  Args:
      x: Top-left x-coordinate of the black square.
      y: Top-left y-coordinate of the black square.

  Returns:
      A NumPy array representing the image.
  """

  # Image dimensions and data type
  width, height, channels = 1080, 1920, 3
  image = np.zeros((width, height, channels), dtype=np.uint8)

  # Set the entire image to white
  image[:] = (255, 255, 255)

  # Draw a black square
  square_size = 10
  image[x:x+square_size, y:y+square_size] = (0, 0, 0)

  return image

# Set the square coordinates (modify these for different positions)
x_coord = 200
y_coord = 300

# Generate the image
image = f(x_coord, y_coord)

# Plot the image
plt.imshow(image)
plt.axis('off')  # Hide axes for cleaner visualization
plt.title("White Image with Black Square")
plt.show()
