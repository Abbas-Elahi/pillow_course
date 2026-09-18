from PIL import Image
import matplotlib.pyplot as plt

# Load the image
img = Image.open('Nature.jpg')

# Create a figure for all images
fig, axes = plt.subplots(2, 3, figsize=(10, 6))
fig.suptitle('Image Processing with Pillow', fontsize=16, fontweight='bold')

# Display original image
axes[0, 0].imshow(img)
axes[0, 0].set_title('Original Image')
axes[0, 0].axis('off')

# Resize
resized = img.resize((800, 600))
axes[0, 1].imshow(resized)
axes[0, 1].set_title('Resized (800×600)')
axes[0, 1].axis('off')

# Rotate 45 degrees
rotated = img.rotate(45, expand=True)
axes[0, 2].imshow(rotated)
axes[0, 2].set_title('Rotated 45°')
axes[0, 2].axis('off')

# Horizontal flip (mirror)
mirror = img.transpose(Image.FLIP_LEFT_RIGHT)
axes[1, 0].imshow(mirror)
axes[1, 0].set_title('Horizontal Flip')
axes[1, 0].axis('off')

# Vertical flip
flip = img.transpose(Image.FLIP_TOP_BOTTOM)
axes[1, 1].imshow(flip)
axes[1, 1].set_title('Vertical Flip')
axes[1, 1].axis('off')

# Crop
box = (100, 100, 400, 400)
cropped = img.crop(box)
axes[1, 2].imshow(cropped)
axes[1, 2].set_title(f'Cropped {box}')
axes[1, 2].axis('off')

# Adjust layout and display
plt.tight_layout()
plt.show()

