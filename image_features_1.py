from PIL import Image

# Open the image
img = Image.open(r"D:\aba_git\pillow_course\img\Nature.jpg")
print(type(img))

print("=" * 50)
print(f" Filename: {img.filename}")
print("=" * 50)

# 1. Main properties
print(f" Dimensions: {img.size} pixels (width × height)")
print(f" Width: {img.width} pixels")
print(f" Height: {img.height} pixels")
print(f" Color mode: {img.mode}")
print(f" Format: {img.format}")


img.show()
