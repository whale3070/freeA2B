from PIL import Image

def compress_image(input_image_path, output_image_path, quality=85):
    """
    Function to compress an image.
    
    Parameters:
    - input_image_path (str): Path to the input image (JPEG or PNG).
    - output_image_path (str): Path to save the output compressed image.
    - quality (int): Quality level for JPEG compression (1-100, default is 85).
    """
    image = Image.open(input_image_path)
    
    # Save as JPEG or PNG based on input image format
    if image.format == 'JPEG':
        image.save(output_image_path, quality=quality, optimize=True)
    elif image.format == 'PNG':
        image.save(output_image_path, optimize=True)
    else:
        raise ValueError("Unsupported image format. Only JPEG and PNG are supported.")

# Get user input for image file name
input_image_name = input("Enter the name of the image file (with extension): ")

# Example paths
input_image_path = input_image_name
output_image_path = 'output_compressed.jpg'  # Output file path, you can modify as needed

# Compress the image
compress_image(input_image_path, output_image_path, quality=70)

print(f"Image compressed and saved as {output_image_path}")
