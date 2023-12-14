import time
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont

# Create an SSD1306 OLED object.
disp = Adafruit_SSD1306.SSD1306_128_32(rst=None)

# Initialize the library.
disp.begin()

# Clear the display.
disp.clear()
disp.display()

# Create a blank image for drawing.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get a drawing object.
draw = ImageDraw.Draw(image)

# Load default font.
font = ImageFont.load_default()

def display_text(text):
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    # Split the text into lines that fit the display width.
    lines = []
    line = []
    line_width = 0
    words = text.split(' ')
    for word in words:
        word_width, word_height = draw.textsize(' '.join(line + [word]), font=font)
        if word_width > width:
            # This line is full, store it and start a new one.
            lines.append(' '.join(line))
            line = [word]
        else:
            line.append(word)
    # Store the last line.
    lines.append(' '.join(line))

    # Write each line to the display, scrolling up for each new line.
    for line in lines:
        draw.text((0, 0), line, font=font, fill=255)
        disp.image(image)
        disp.display()
        time.sleep(0.5)
        draw.rectangle((0,0,width,height), outline=0, fill=0)

# Test the function with your text.
display_text("This is a test of the OLED text display function.")
