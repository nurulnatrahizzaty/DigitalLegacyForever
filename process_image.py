import os

from PIL import Image

# Path to the image
image_path = r"c:\Users\user\Documents\LEGACY_DIGITAL_FOREVER_PROTOTYP\LEGACY_DIGITAL_FOREVER_PROTOTYP\static\images\image_digital legacy.jpg"

# Open the image
img = Image.open(image_path)
print(f"Original size: {img.size}")

# Assume the frame is 20 pixels from each side
crop_margin = 20
width, height = img.size
if width > 2 * crop_margin and height > 2 * crop_margin:
    img_cropped = img.crop(
        (crop_margin, crop_margin, width - crop_margin, height - crop_margin)
    )
else:
    img_cropped = img

print(f"Cropped size: {img_cropped.size}")

# Now keep the same size, no resize
img_resized = img_cropped

# Save the new image, perhaps overwrite or save as new
output_path = image_path.replace(".jpg", "_processed.jpg")
img_resized.save(output_path)

print(f"Processed image saved to {output_path}")

print(f"Processed image saved to {output_path}")
