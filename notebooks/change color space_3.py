from PIL import Image
from pathlib import Path


def convert_for_specific_use(image_path):
    img = Image.open(image_path)

    print(f"Original image - Mode: {img.mode}, Size: {img.size}")

    save_dir = Path(r"D:\aba_git\pillow_course\save")
    save_dir.mkdir(parents=True, exist_ok=True)

    # 1. Convert for computer vision (typically grayscale)
    gray_for_cv = img.convert("L")
    gray_for_cv.save(save_dir / "for_computer_vision.jpg")
    print(f"For computer vision: Mode {gray_for_cv.mode}")

    # 2. Convert for printing (CMYK)
    cmyk_for_print = img.convert("CMYK")
    cmyk_for_print.save(save_dir / "for_print.tif")
    print(f"For printing: Mode {cmyk_for_print.mode}")

    # 3. Convert for web
    rgb_for_web = img.convert("RGB")
    rgb_for_web.save(save_dir / "for_web.jpg", quality=85, optimize=True)
    print(f"For web: Mode {rgb_for_web.mode}")

    # 4. Convert to pure black and white (for text)
    bw_for_text = img.convert("1")
    bw_for_text.save(save_dir / "for_text.png")
    print(f"For text: Mode {bw_for_text.mode}")


# Call the function
convert_for_specific_use(r"D:\aba_git\pillow_course\img\Nature.jpg")
