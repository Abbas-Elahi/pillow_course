from PIL import Image

# Open the image
img = Image.open('Nature.jpg')

# Direct pixel access
pixels = img.load()

# Modify each pixel's color
for i in range(img.width):
    for j in range(img.height):
        r, g, b = pixels[i, j]

        # Remove red color
        pixels[i, j] = (0, g, b)

img.show()
