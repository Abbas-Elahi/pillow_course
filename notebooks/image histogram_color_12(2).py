from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('Nature.jpg')

# Separate color channels
r, g, b = img.split()

# Calculate histogram for each channel
hist_r = r.histogram()
hist_g = g.histogram()
hist_b = b.histogram()

# Display histograms
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(img)
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.bar(range(256), hist_r[:256], color='red', alpha=0.6, label='Red')
plt.title('Red Channel Histogram')
plt.xlabel('Intensity')
plt.ylabel('Frequency')
plt.legend()

plt.subplot(2, 2, 3)
plt.bar(range(256), hist_g[:256], color='green', alpha=0.6, label='Green')
plt.title('Green Channel Histogram')
plt.xlabel('Intensity')
plt.ylabel('Frequency')
plt.legend()

plt.subplot(2, 2, 4)
plt.bar(range(256), hist_b[:256], color='blue', alpha=0.6, label='Blue')
plt.title('Blue Channel Histogram')
plt.xlabel('Intensity')
plt.ylabel('Frequency')
plt.legend()

plt.tight_layout()
plt.show()

