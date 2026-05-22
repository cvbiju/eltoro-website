import cv2
import numpy as np
import sys

img_path = 'public/assets/images/biju_bg.png'
out_path = 'public/assets/images/biju_light.png'

# Load the image
img = cv2.imread(img_path)
if img is None:
    print(f"Could not load image {img_path}")
    sys.exit(1)

# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(np.float32)

# Split channels
h, s, v = cv2.split(hsv)

# Normalize V to 0.0 - 1.0
v_norm = v / 255.0

# Apply gamma correction to lift shadows
# A gamma between 0.5 to 0.7 is usually good for heavy shadows
gamma = 0.65
v_light = np.power(v_norm, gamma) * 255.0

# Clip values to 0-255 just in case
v_light = np.clip(v_light, 0, 255).astype(np.uint8)
h = h.astype(np.uint8)
s = s.astype(np.uint8)

# Merge back into HSV
hsv_light = cv2.merge([h, s, v_light])

# Convert back to BGR
out_img = cv2.cvtColor(hsv_light, cv2.COLOR_HSV2BGR)

# Apply a gentle contrast boost since lifting shadows might fade the picture
# using CLAHE (Contrast Limited Adaptive Histogram Equalization) on the lightness channel of LAB could be better,
# but a simple alpha/beta contrast boost works too.
alpha = 1.1 # Contrast control (1.0-3.0)
beta = -10  # Brightness control (0-100)
out_img = cv2.convertScaleAbs(out_img, alpha=alpha, beta=beta)

cv2.imwrite(out_path, out_img)
print(f"Saved brightened image to {out_path}")
