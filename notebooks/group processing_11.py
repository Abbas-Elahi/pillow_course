from PIL import Image
import os

# 1. Define folders
input_folder = "input_images"
output_folder = "resized_images"

os.makedirs(output_folder, exist_ok=True)  # Create output folder if it doesn't exist

# 2. Process all images in the folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.png', '.jpeg')):  # Process only image files
        filepath = os.path.join(input_folder, filename)

        # 3. Open and resize image (EXACT size, no aspect ratio preservation)
        img = Image.open(filepath)
        img_resized = img.resize((200, 200))  # Force exact 200x200 pixels

        # 4. Save to new folder
        output_path = os.path.join(output_folder, filename)
        img_resized.save(output_path)

        print(f" {filename} resized to exact 200x200 and saved.")

print("All images processed successfully!")

