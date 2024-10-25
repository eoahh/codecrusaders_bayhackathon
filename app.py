import numpy as np
from PIL import Image
import io

def process_image(image_data):
    # Load the image and convert it to grayscale
    image = Image.open(io.BytesIO(image_data)).convert("L")
    image_array = np.array(image)

    # Calculate mean and standard deviation of grayscale values
    mean_value = np.mean(image_array)
    std_dev_value = np.std(image_array)

    return {"mean": mean_value, "std_dev": std_dev_value}