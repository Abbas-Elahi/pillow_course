from PIL import Image
import matplotlib.pyplot as plt

# Open the image and convert to grayscale
img = Image.open('Nature.jpg').convert('L')

# Calculate the histogram
histogram = img.histogram()

# Display the histogram
plt.figure(figsize=(10, 5))
plt.bar(range(256), histogram[:256], color='gray', alpha=0.7)
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Intensity (0-255)')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.show()

# Display statistical information
print(f"Total pixels: {sum(histogram[:256])}")
print(f"Mean intensity: {sum(i*histogram[i] for i in range(256))/sum(histogram[:256]):.1f}")

