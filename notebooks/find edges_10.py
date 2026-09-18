from PIL import Image, ImageFilter, ImageEnhance

# Open image
image = Image.open('Nature.jpg').convert('L')  # Convert to grayscale

# Apply edge detection filter
edges = image.filter(ImageFilter.FIND_EDGES)
# Display result
edges.show()

# 1. First, sharpen the image
sharpened = image.filter(ImageFilter.SHARPEN)

# 2. Then apply edge detection
edges = sharpened.filter(ImageFilter.FIND_EDGES)

# 3. Enhance edge contrast
contrast = ImageEnhance.Contrast(edges)
strong_edges = contrast.enhance(2.0)  # 2x contrast

strong_edges.show()

