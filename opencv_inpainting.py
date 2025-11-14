import cv2
import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlretrieve

# 1. Download a sample image (you can change this URL)
image_url = "https://i.imgur.com/gK8L833.jpeg" 
image_file = "sample_input.jpg"
urlretrieve(image_url, image_file)

# 2. Load the image
img = cv2.imread(image_file)
# Convert from BGR (OpenCV default) to RGB (Matplotlib/standard display)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 3. Create the Mask: Define a white area on a black background
# We'll create a simple white rectangle mask for demonstration.
mask = np.zeros(img.shape[:2], dtype="uint8")

# Define the coordinates for the area to be masked (e.g., removing the large sign/building)
# The area is defined by: mask[y_start:y_end, x_start:x_end]
mask[100:300, 200:500] = 255 

# 4. Run the Inpainting Algorithm
result_telea = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

# Convert the result back to RGB for display
result_telea_rgb = cv2.cvtColor(result_telea, cv2.COLOR_BGR2RGB)

# 5. Display Results
def display_images(original, mask, inpainted):
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # Original Image
    axes[0].imshow(original)
    axes[0].set_title("1. Original Image")
    axes[0].axis('off')

    # Mask
    axes[1].imshow(mask, cmap='gray')
    axes[1].set_title("2. Inpaint Mask (White Area to Fill)")
    axes[1].axis('off')
    
    # Inpainted Result
    axes[2].imshow(inpainted)
    axes[2].set_title("3. Inpainted Result (Telea)")
    axes[2].axis('off')
    
    plt.show()

# Run the display function
display_images(img_rgb, mask, result_telea_rgb)