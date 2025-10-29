from PIL import Image
import numpy as np
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfgen import canvas


# List of ASCII characters representing brightness levels
# (from dark → light)
char_list = [' ', '.', ',', ':', ';', '-', '~', '=', '^', '*', '+', 'o', 'x', 'p', '2', 'C', 'H', 'X', 'Q', 'M', '&', '#', '@'] 


# Converts image into a resized grayscale NumPy array
def grayArray(image_path):

    with Image.open(image_path) as img:

        # Convert image to grayscale ('L' mode = luminance)
        image = img.convert('L')
        x, y = image.size[0], image.size[1]

        new_x, new_y = 300, int(y / (x / 360))              # maintain aspect ratio

        grayscale_img =  image.resize((new_x, new_y))       
        img_array = np.array(grayscale_img)

         # Return both the image array and the size of the page (scaled slightly wider)
        return img_array, (new_x*1.2, new_y)


# Input image path
image_path = "ASCII_art\\image.jpg"
arr, shape = grayArray(image_path)


# Create PDF canvas with custom size = image shape
pdf = canvas.Canvas("ASCII_art\\image.pdf", pagesize=shape)

# --- Background ---
pdf.setFillColorRGB(0, 0, 0)  # black
pdf.rect(0, 0, shape[0], shape[1], fill=1)


# --- Text settings ---
pdf.setFillColorRGB(1, 1, 1)        # White text
pdf.setFont("Courier-Bold", 1)      # Monospaced font (essential for ASCII art)


# --- Draw ASCII art line by line ---
i = 0

for x in arr:
    
    l = ''

    for y in x:

        char = int((int(y) + 1) // 11.15)       # Convert pixel (0–255) to character index (0–len(char_list)-1)
        l += f"{char_list[char]*2}"             # Append the character twice (for horizontal density)
    pdf.drawString(0, shape[1] - i, l)          # Draw the ASCII line at decreasing y-coordinate
    i += 1                                      # Move to next line

pdf.save()
