from PIL import Image, ImageDraw, ImageFont

# =======================================CREATING A WHITE CANVAS
width, height = 500, 500
image = Image.new('RGB', (width, height), color='white')
draw = ImageDraw.Draw(image)

# ========================================DRAWING LINES
# Draw a line from (x1, y1) to (x2, y2)
# Parameters: (start_x, start_y, end_x, end_y), fill=color, width=thickness
draw.line((350, 350, 450, 500), fill='blue', width=3)          # Horizontal line
draw.line([(30, 30), (100, 150), (200, 100)], fill='green', width=2)  # Polyline

image.show()
input("Press Enter to see the next image...")

# ====================================DRAWING RECTANGLES
# Filled rectangle
# (left-top, right-bottom)
draw.rectangle((150, 250, 250, 350), fill='blue', outline='black', width=2)

# Empty rectangle (only outline)
draw.rectangle((100, 250, 350, 450), fill=None, outline='red', width=3)

# Rectangle with rounded corners
draw.rounded_rectangle((270, 380, 400, 480), radius=20, fill='green', outline='black', width=2)

image.show()
input("Press Enter to see the next image...")

# =====================================DRAWING CIRCLES AND ELLIPSES
# Filled circle (using bounding box)
draw.ellipse((300, 50, 500, 150), fill='red', outline='black', width=2)

# Empty circle
draw.ellipse((200, 50, 300, 150), fill=None, outline='blue', width=3)

image.show()
input("Press Enter to see the next image...")

# =======================================DRAWING POLYGONS
# Triangle
draw.polygon([(400, 400), (300, 200), (500, 400)], fill='lightblue', outline='blue', width=2)

# Pentagon
draw.polygon([(200, 100), (250, 150), (230, 220), (170, 220), (150, 150)],
             fill='lightgreen', outline='darkgreen', width=2)

# 5-pointed star
star_points = [
    (200, 300), (220, 340), (260, 340),  # Start from the top of the star
    (230, 360), (245, 400),              # Continue points
    (200, 375), (155, 400), (170, 360),  # Bottom points
    (140, 340), (180, 340)               # Points back to the top
]
draw.polygon(star_points, fill='gold', outline='orange', width=2)

image.show()
input("Press Enter to see the next image...")

# ========================================DRAWING ARCS, PIES, AND CHORDS
# Arc (only the outline)
# Parameters: bounding_box, start_angle, end_angle, fill
draw.arc((50, 50, 150, 150), start=45, end=270, fill='red', width=3)

# Pie slice (like a pizza slice)
draw.pieslice((200, 50, 300, 150), start=30, end=120, fill='blue', outline='black', width=2)

# Chord (arc with a straight line connecting the ends)
draw.chord((50, 180, 250, 280), start=0, end=180, fill='green', outline='darkgreen', width=2)

image.show()
input("Press Enter to see the next image...")

# =========================================DRAWING A SMILEY FACE
# Face (large circle)
draw.ellipse((50, 50, 250, 250), fill='yellow', outline='orange', width=3)

# Left eye (circle)
draw.ellipse((100, 100, 120, 120), fill='black')
# Right eye
draw.ellipse((180, 100, 200, 120), fill='black')

# Mouth (arc)
draw.arc((100, 130, 200, 200), start=0, end=180, fill='black', width=5)

# Cheeks (small circles)
draw.ellipse((80, 160, 90, 170), fill='pink')
draw.ellipse((210, 160, 220, 170), fill='pink')

image.show()
input("Press Enter to see the next image...")
# ========================================DRAWING Text
font=ImageFont.truetype('arial.ttf', size=40)
draw.text((50, 450), "Hello, Pillow!", fill=(255,0,255,255), font=font)

image.show()

