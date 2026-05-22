import sys
from PIL import Image

try:
    from rembg import remove
except ImportError:
    print("rembg not installed")
    sys.exit(1)

# Get the background color from Suzy's image
suzy_img = Image.open('public/assets/images/6.png')
# Provide a fallback, or just read pixel 0,0
bg_color = suzy_img.getpixel((0, 0))
if isinstance(bg_color, int):
    # If grayscale
    bg_color = (bg_color, bg_color, bg_color)
elif len(bg_color) == 4:
    bg_color = bg_color[:3] # RGB

print("Background color extracted:", bg_color)

# Open Biju's image
biju_img = Image.open('public/assets/images/biju_new.png')

# Remove background
print("Removing background from biju_new.png...")
biju_nobg = remove(biju_img)

# Create a new image with the identical background color
print("Creating solid background...")
final_img = Image.new("RGBA", biju_nobg.size, bg_color + (255,))

# Paste the no-bg image over the background
# The third argument is the mask
final_img.paste(biju_nobg, (0, 0), biju_nobg)

# Convert to RGB to save as jpg or keep as png, let's keep as png 
final_img = final_img.convert("RGB")
final_img.save('public/assets/images/biju_bg.png')
print("Saved as biju_bg.png")
