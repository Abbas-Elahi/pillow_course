from PIL import Image

def convert_for_specific_use(image_path):
    img = Image.open(image_path)

    print(f"Original image - Mode: {img.mode}, Size: {img.size}")

    # 1. Convert for computer vision (typically grayscale)
    gray_for_cv = img.convert('L')
    gray_for_cv.save('for_computer_vision.jpg')
    print(f"For computer vision: Mode {gray_for_cv.mode}")

    # 2. Convert for printing (CMYK)
    cmyk_for_print = img.convert('CMYK')
    cmyk_for_print.save('for_print.tif')
    print(f"For printing: Mode {cmyk_for_print.mode}")

    # 3. Convert for web
    rgb_for_web = img.convert('RGB')
    rgb_for_web.save('for_web.jpg', quality=85, optimize=True)
    print(f"For web: Mode {rgb_for_web.mode}")

    # 4. Convert to pure black and white (for text)
    bw_for_text = img.convert('1')
    bw_for_text.save('for_text.png')
    print(f"For text: Mode {bw_for_text.mode}")

# Call the function
convert_for_specific_use('Nature.jpg')
