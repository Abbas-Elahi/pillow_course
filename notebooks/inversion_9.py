from PIL import Image, ImageOps
import matplotlib.pyplot as plt

# Open the image
img = Image.open('Nature.jpg')

# Invert the colors
inverted_img = ImageOps.invert(img)

# Display with Matplotlib for proper titles
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

ax1.imshow(img)
ax1.set_title('Original Image')
ax1.axis('off')

ax2.imshow(inverted_img)
ax2.set_title('Inverted Image')
ax2.axis('off')

plt.tight_layout()
plt.show()

