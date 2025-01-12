import os

from PIL import Image


def rgb_to_indexed_image(rgb_image_path, indexed_image_path, palette_path=None):
    # Open the RGB image
    rgb_image = Image.open(rgb_image_path).convert("RGB")

    # Create a palette (optional)
    if palette_path:
        # Load the palette from a file
        with open(palette_path, 'r') as f:
            palette_lines = f.readlines()

        # Parse the palette
        palette = []
        for line in palette_lines:
            rgb_values = line.strip().split()
            if len(rgb_values) == 3:
                r, g, b = map(int, rgb_values)
                palette.extend([r, g, b, 255])  # Add alpha channel (fully opaque)

        # Ensure the palette has 256 colors (768 values, 3 RGB + 1 Alpha per color)
        if len(palette) < 768:
            palette.extend([0, 0, 0, 255] * (256 - len(palette) // 4))

    else:
        # Generate a default palette (optional)
        palette = []
        for i in range(256):
            palette.extend([i, i, i, 255])  # Grayscale palette with full opacity

    # Convert the RGB image to an indexed image using the palette
    indexed_image = rgb_image.convert("P", palette=Image.ADAPTIVE, colors=256)

    # Set the palette if provided
    if palette_path:
        indexed_image.putpalette(palette)

    # Save the indexed image
    indexed_image.save(indexed_image_path)
    print(f"Indexed image saved to: {indexed_image_path}")

if __name__ == "__main__":
    # Paths
    rgb_image_dir = r'E:\DataSets\sar_rarp50\training_set_2\video_01\segmentation'
    indexed_image_dir = r'E:\DataSets\sar_rarp50\training_set_2\video_01\segmentation_idx'
    if not os.path.exists(indexed_image_dir):
        os.makedirs(indexed_image_dir)
    for img_name in os.listdir(rgb_image_dir):
        img_path=os.path.join(rgb_image_dir, img_name)
        idx_path=os.path.join(indexed_image_dir,img_name)
        # Call the function to convert the RGB image to an indexed image
        rgb_to_indexed_image(img_path, idx_path)
