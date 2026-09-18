from PIL import Image, ImageEnhance

# Load the image
img = Image.open('Nature.jpg')

# Adjust brightness
brightness = ImageEnhance.Brightness(img)
brighter = brightness.enhance(1.5)  # 1.5 times brighter
brighter.show(title='brighter.jpg')

# Adjust contrast
contrast = ImageEnhance.Contrast(img)
high_contrast = contrast.enhance(2.0)  # Double the contrast
high_contrast.show(title='high_contrast.jpg')

# Adjust color saturation (only for RGB images)
if img.mode == 'RGB':
    saturation = ImageEnhance.Color(img)
    vibrant = saturation.enhance(1.8)  # More vibrant colors
    vibrant.show(title='vibrant.jpg')

'''
final_img = ImageEnhance.Brightness(img).enhance(1.3)
final_img = ImageEnhance.Contrast(final_img).enhance(1.5)
final_img = ImageEnhance.Color(final_img).enhance(1.2)
final_img.show()
'''
