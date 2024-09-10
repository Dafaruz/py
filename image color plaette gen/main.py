from sklearn.cluster import KMeans
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


# Function to load and resize the image
def load_image(image_path, size=(150, 150)):
    img = Image.open(image_path)
    img = img.resize(size)  # Resize image for faster processing
    return img


# Function to extract colors using KMeans
def get_colors(image, num_colors=5):
    # Convert image to numpy array
    image_np = np.array(image)
    image_np = image_np.reshape((image_np.shape[0] * image_np.shape[1], 3))  # Flatten the image pixels

    # KMeans to find the dominant colors
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(image_np)

    return kmeans.cluster_centers_  # Returns the RGB values of the dominant colors


# Function to display the color palette
def show_palette(colors):
    # Create a square showing each color in the palette
    palette = np.zeros((50, 300, 3), dtype="uint8")
    steps = 300 // len(colors)

    for i, color in enumerate(colors):
        palette[:, i * steps:(i + 1) * steps] = color

    plt.figure(figsize=(8, 2))
    plt.axis('off')
    plt.imshow(palette)
    plt.show()


# Main function
def generate_color_palette(image_path, num_colors=5):
    # Load and resize image
    image = load_image(image_path)

    # Extract dominant colors
    colors = get_colors(image, num_colors)

    # Convert colors to integers
    colors = colors.astype(int)

    # Display the color palette
    show_palette(colors)


# Input the image file path
image_path = input("Enter the path to your image file: ")

# Generate the color palette
generate_color_palette(image_path)
