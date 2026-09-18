from PIL import Image

# Open an image file
img = Image.open('Nature.jpg')

# Convert and save in different formats
img.save('output.png')   # Save as PNG
img.save('output.bmp')   # Save as BMP
img.save('output.tiff')  # Save as TIFF

# Save with different quality settings (JPEG only)
img.save('high_quality.jpg', quality=95)  # High quality
img.save('low_quality.jpg', quality=20)   # Low quality

