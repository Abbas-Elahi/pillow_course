from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

img = Image.open('Nature.jpg')

# Blur filter
blurred = img.filter(ImageFilter.BLUR)

# Sharpen filter (edge enhancement)
sharpened = img.filter(ImageFilter.SHARPEN)

# Contour filter (sketched look)
contour = img.filter(ImageFilter.CONTOUR)

# Emboss filter (textured effect)
embossed = img.filter(ImageFilter.EMBOSS)

# Smooth filter
smoothed = img.filter(ImageFilter.SMOOTH)

plt.figure(figsize=(10, 6))

plt.subplot(2, 3, 1)
plt.imshow(img)
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(blurred)
plt.title('Blurred Image')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(sharpened)
plt.title('Sharpen Image')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(contour)
plt.title('Contour Image')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(embossed)
plt.title('Emboss Image')
plt.axis('off')

plt.subplot(2, 3, 6)
plt.imshow(smoothed)
plt.title('Smooth Image')
plt.axis('off')

plt.tight_layout()
plt.show()
